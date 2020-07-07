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

# mutate boolean_symbols
def boolean_symbols_check(origin=""):
    boolean_symbols = (">","<",">=","<=","==","!=") #布林運算符號
    bl_rs_symbols = list(boolean_symbols)
    mutations = [] #存放變異體

    for i,symbol in enumerate(boolean_symbols): #檢查布林運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引

            if symbol == ">" or symbol == "<": #確定不是>=或<=
                for (j,confirm) in enumerate(all_willberp_index):
                    if origin[confirm:confirm+2] == "<=" or origin[confirm:confirm+2] == ">=":
                        del(all_willberp_index[j])
            print("當前的symbol",symbol)
            print('nows symbols',bl_rs_symbols[i],'i=',i)
            print("刪除前的bl_rs_symbols=",bl_rs_symbols)
            del bl_rs_symbols[i] #把不必變異的符號刪除
            print('刪除後的bl_rs_symbols=',bl_rs_symbols)
            print('所有該被替換的符號',all_willberp_index,'\n')

            for index in all_willberp_index:
                if len(symbol) == 1: #如果是< >
                    print(symbol,'\n-----')
                    for rpsym in bl_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+1):])
                else:#如果是 != == <= =>
                    for rpsym in bl_rs_symbols:
                        print(symbol,'\n_______')
                        mutations.append(origin[:index] + rpsym + origin[(index+2):])

            bl_rs_symbols = list(boolean_symbols)
            all_willberp_index = []
    return mutations