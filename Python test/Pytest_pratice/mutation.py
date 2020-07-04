import os

def get_index(string=None, item=''):
    flag = 0
    all_index = []

    for value in string:
        if string.find(item,flag) != -1:
           all_index.append(string.find(item,flag))            
           flag =  string.find(item,flag) + 1
        else:break
    return all_index
    
boolean_symbols = {">","<",">=","<=","==","!="} #布林運算符號
print(boolean_symbols,"\n\n\n\n\n\n")
opration_symbols = {"+","-","*","/"} #運算符號
bl_rs_symbols = list(boolean_symbols)
op_rs_symbols = list(opration_symbols)
mutations = [] #存放變異體

with open('threefive.py', 'r', encoding='UTF-8') as file:
    origin = file.read() #讀入要做測試的程式
    #mut_origin = origin
    for i,symbol in enumerate(boolean_symbols): #檢查布林運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            if symbol == ">" or symbol == "<": #確定不是>=或<=
                for (i,confirm) in enumerate(all_willberp_index):
                    if origin[confirm:confirm+2] == "<=" or origin[confirm:confirm+2] == ">=":
                        del(all_willberp_index[i])

            del bl_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:
                if len(symbol) == 1: #如果是< >
                    for rpsym in bl_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+1):])
                else:#如果是 != == <= =>
                    for rpsym in bl_rs_symbols:
                        mutations.append(origin[:index] + rpsym + origin[(index+2):])
            bl_rs_symbols = list(boolean_symbols)

    for i,symbol in enumerate(opration_symbols): #檢查運算符號
        if symbol in origin:
            all_willberp_index = get_index(origin, symbol) #獲取相符的所有索引
            del op_rs_symbols[i] #把不必變異的符號刪除
            for index in all_willberp_index:    
                for rpsym in op_rs_symbols:
                    mutations.append(origin[:index] + rpsym + origin[(index+1):])
            op_rs_symbols = list(opration_symbols)

mu_filenames = [] #存放變異體的檔案名稱
for i,item in enumerate(mutations): #產生變異體檔案出來
    filename = "test_" + str(i) + ".py"
    mu_filenames.append("test_" + str(i))
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(item)

for mus in mu_filenames:
    output = os.system("pytest test_assert.py")