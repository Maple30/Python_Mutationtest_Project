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
                    if origin[confirm:confirm+2] == "<=" or origin[confirm:confirm+2] == ">=":
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
    mutation = []
    for i,symbol in enumerate(opration_symbols): #檢查運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del op_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                for rpsym in op_rs_symbols:
                    mutation.append(origin[:index] + rpsym + origin[(index+1):])
            op_rs_symbols = list(opration_symbols)
    return mutation
# mutate logic_symbols
def logic_symbols_check(origin=""):
    logic_symbols = ("and","or") #邏輯符號
    lo_rs_symbols = list(logic_symbols)
    mutation = []
    for i,symbol in enumerate(logic_symbols): #檢查邏輯符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del lo_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                if symbol == "and":
                    for rpsym in lo_rs_symbols:
                        mutation.append(origin[:index] + rpsym + origin[(index+3):])
                elif symbol == "or":
                    for rpsym in lo_rs_symbols:
                        mutation.append(origin[:index] + rpsym + origin[(index+2):])
            lo_rs_symbols = list(logic_symbols)
    return mutation

# mutate binary_symbols
def binary_symbols_check(origin=""):
    binary_symbols = ("&","|","^",">>","<<") #邏輯符號
    bi_rs_symbols = list(binary_symbols)
    mutation = []
    for i,symbol in enumerate(binary_symbols): #檢查邏輯符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del bi_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                if symbol == "and":
                    for rpsym in bi_rs_symbols:
                        mutation.append(origin[:index] + rpsym + origin[(index+3):])
                elif symbol == "or":
                    for rpsym in bi_rs_symbols:
                        mutation.append(origin[:index] + rpsym + origin[(index+2):])
            bi_rs_symbols = list(binary_symbols)
    return mutation