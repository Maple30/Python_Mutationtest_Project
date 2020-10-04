def get_index(trash_test_word=None, item=''):
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
                        # print("我進到了是and的地方")
                        
                        all_index.append(Now_position + ele.find(item,flag))
                        # print(Now_position, ele.find(item,flag))
                        # print(all_index)
                        
                        flag =  ele.find(item,flag) + 1
            else:
                break
        Now_position += index_lenth_list[i]
    # print(len(index_lenth_list))
    # print(all_index)

    return all_index

# origin = "Num = ccccc\n if a and b "
origin = "def test_game(Ascending_power_Num):\n    Descending_power_Num = 0\n    Appeared_Num = []\n    New_num = 0\n\n    while(1):\n        Ascending_power_Num = list(map(int,Ascending_power_Num))\n        Ascending_power_Num.sort(reverse=True)\n        Descending_power_Num = sorted(Ascending_power_Num)\n\n        New_num = int("".join([str(X) for X in Ascending_power_Num])) - int("".join([str(Y) for Y in Descending_power_Num]))\n        New_num = str(New_num)\n        Ascending_power_Num = New_num\n\n        if New_num in Appeared_Num:\n            return len(Appeared_Num) + 1\n        else:\n            Appeared_Num.append(New_num)\n            Ascending_power_Num = New_num\n            if A and B:"

logic_symbols = ("and","or") #邏輯符號
lo_rs_symbols = list(logic_symbols)
mutations = []
all_willberp_index = []

for i,symbol in enumerate(logic_symbols): #檢查邏輯符號
    if symbol in origin:
        all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引

        # print(type(all_willberp_index))
        del lo_rs_symbols[i] #把不必變異的符號刪除
        for index in all_willberp_index:
            if symbol == "and":
                for rpsym in lo_rs_symbols:
                    mutations.append(origin[:index] + rpsym + origin[(index+3):])
                    # print()
            elif symbol == "or":
                for rpsym in lo_rs_symbols:
                    mutations.append(origin[:index] + rpsym + origin[(index+2):])
        lo_rs_symbols = list(logic_symbols)

# print(len(origin))
    try:
        print(origin[all_willberp_index[0]])
    except:
        print("failed")

# print(all_willberp_index)
# print(mutations)
# for i in mutations:
#     print(i)

#藥用外面的字串來確認位置