# 取小數點第n位
def get_two_float(f_str, n):
    f_str = str(f_str)
    a, b, c = f_str.partition('.')
    c = (c+"0"*n)[:n]       # 補0
    return ".".join([a, c])

# find out which symbol need to be replaced for and or
def get_index_for_or(trash_test_word=None, item=''):
    all_index = []
    index_lenth_list = []
    A = trash_test_word.split("\n")
    Now_position = 0
    flag = 0
    
    for cut,i in enumerate(A):
        if len(A)-1 == cut:
            index_lenth_list.append(len(i))
        index_lenth_list.append(len(i) + 1)
        
        # print(len(i))
    
    for i,ele in enumerate(A):
        if item in ele:
            if "print" in ele.split("(")[0]:
                Now_position += index_lenth_list[i]
                continue
        for value in ele:
            if ele.find(item, flag) != -1:
                if item == "or":
                    if ele[ele.find(item,flag)-1] != " " or ele[ele.find(item,flag)+2] != " ":
                        continue
                    else:
                        print("我進到了是or的地方")
                        all_index.append(Now_position + ele.find(item,flag))
                        flag =  ele.find(item,flag) + 1
                        
                elif item == "and":
                    if ele[ele.find(item,flag)-1] != " " or ele[ele.find(item,flag)+3] != " ":
                        # print("我進到了不是and的地方")
                        continue
                    else:
                        # print(Now_position, len(trash_test_word))
                        print("我進到了是and的地方")
                        
                        all_index.append(Now_position + ele.find(item,flag))
                        # print(Now_position, ele.find(item,flag))
                        # print(all_index)
                        
                        flag =  ele.find(item,flag) + 1
            else:
                break
        Now_position += index_lenth_list[i]
    # print(len(index_lenth_list))
    print(all_index)

    return all_index

# find out which symbol need to be replaced
def get_index(string=None, item=''):
    flag = 0
    all_index = []

    for value in string:
        if string.find(item,flag) != -1:
           all_index.append(string.find(item,flag))
           flag =  string.find(item,flag) + 1
        else:
            break
    return all_index

# mutate relation_symbols
def relation_symbols_check(origin=""):
    relation_symbols = (">","<",">=","<=","==","!=") #布林運算符號
    re_rs_symbols = list(relation_symbols)
    mutations = [] #存放變異體

    for i,symbol in enumerate(relation_symbols): #檢查布林運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引

            if symbol == ">" or symbol == "<": #確定不是>=或<=
                for (j,confirm) in enumerate(all_willberp_index):
                    if origin[confirm:confirm+2] == "<=" or origin[confirm:confirm+2] == ">=" or origin[confirm:confirm+2] == ">>" or origin[confirm:confirm+2] == "<<":
                        del(all_willberp_index[j])
            del re_rs_symbols[i] #把不必變異的符號刪除

            for index in all_willberp_index:
                if len(symbol) == 1: #如果是< >
                    for rpsym in re_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+1):])
                else:#如果是 != == <= =>
                    for rpsym in re_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+2):])

            re_rs_symbols = list(relation_symbols)
            all_willberp_index = []

    return mutations

# mutate opration_symbols
def opration_symbols_check(origin=""):
    opration_symbols = ("+","-","*","/","%") #運算符號
    op_rs_symbols = list(opration_symbols)
    mutations = []
    for i,symbol in enumerate(opration_symbols): #檢查運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del op_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                for rpsym in op_rs_symbols:
                    mutations.append(origin[:index] + rpsym + origin[(index+1):])
            op_rs_symbols = list(opration_symbols)
    return mutations
# mutate logic_symbols
def logic_symbols_check(origin=""):
    logic_symbols = ("and","or") #邏輯符號
    lo_rs_symbols = list(logic_symbols)
    mutations = []
    for i,symbol in enumerate(logic_symbols): #檢查邏輯符號
        if symbol in origin:
            all_willberp_index = get_index_for_or(origin, symbol) #獲取相符的所有索引
            del lo_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                if symbol == "and":
                    for rpsym in lo_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+3):])
                elif symbol == "or":
                    for rpsym in lo_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+2):])
            lo_rs_symbols = list(logic_symbols)
    return mutations

# mutate binary_symbols
def binary_symbols_check(origin=""):
    binary_symbols = ("&","|","^",">>","<<") #邏輯符號
    bi_rs_symbols = list(binary_symbols)
    mutations = []
    for i,symbol in enumerate(binary_symbols): #檢查邏輯符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del bi_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                if len(symbol) == 1: #如果是& | ^
                    for rpsym in bi_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+1):])
                else:#如果是 >> <<
                    for rpsym in bi_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+2):])
            bi_rs_symbols = list(binary_symbols)

    return mutations
# 輸出字串處理
def output_str_hadler(totalprograms, Killper, suvived):
    output_string = []
    output_string.append('Total programs:' + str(totalprograms))
    output_string.append('Killpercentage:' + str(Killper) + '%')
    output_string.append('Total suvived programs:' + str(len(suvived)))
    
    for item in suvived:
        output_string.append(item[0])
        output_string.append("suvived functions:")
        for fucname in item[1:-1]:
            output_string.append(fucname)
        output_string.append("\n"+item[-1])
        output_string.append("")
    # print('i am output_str_hadler','')
    # print(output_string)
    return output_string, Killper

# 計算kill比率並回傳輸出結果
def killpercent(beslipt_output=list(), assert_all_fun = []):
    total = len(beslipt_output)
    killed_counter = 0
    kill_success_test_name = []
    suvived = []
        # with open(i[0], 'r', encoding='UTF-8') as file:
    # print(beslipt_output)
    
    for one in beslipt_output:
        if "passed" in one[-2] and "failed" in one[-2]: 
            for p,item in enumerate(one):
                if "short test summary info" in item:
                    killedfunc = []
                    suvived.append([one[p+1].split("::")[0].split(" ")[1]])
                    
                    if "Testclass" in one[p+1]:
                        for killedstest in one[p+1:-2]:
                            killedfunc.append(killedstest.split("::")[2].split(" ")[0])
                    
                    else:
                        for killedstest in one[p+1:-2]:
                            killedfunc.append(killedstest.split("::")[1].split(" ")[0])
                    
                    for IsTestFucName in one:
                        if "def" in IsTestFucName and "test" in IsTestFucName:
                            suvived[-1].append(IsTestFucName.split(" ")[-1][0:-1])
        elif ("failed" in one[-2]) and ("passed" not in one[-2]): 
            killed_counter += 1
        else: # ("failed" notS in one[-2]) and ("passed" in one[-2]) 只有passed存在
            for p,item in enumerate(one):
                if "[100%]" in item:
                    suvived.append([item.split()[0]])

                    # 將所有function name放入
                    for funName in assert_all_fun:
                        suvived[-1].append(funName)

    # print("bslipt_output = ")
    # print(beslipt_output)
    # print("total = " + str(total))
    # print(suvived)
    for i in suvived:
        with open(i[0], 'r', encoding='UTF-8') as file:
            i.append(file.read())
    print(killed_counter,total)
    return output_str_hadler(total, get_two_float((killed_counter/total)*100,2), suvived)