import os
from functions import *

mutations = [] #存放變異體
with open('threefive.py', 'r', encoding='UTF-8') as file:
    origin = file.read() #讀入要做測試的程式
    
    mutations += relation_symbols_check(origin)# relation_symbols
    mutations += opration_symbols_check(origin)#opration_symbols
    mutations += logic_symbols_check(origin)# logic_symbols
    mutations += binary_symbols_check(origin)# binary_symbols
# print(mutations)
AssertPart = "" ##讀入assert code 進行改寫
with open("test_assert.py",'r',encoding="UTF-8") as file:
    AssertPart = file.read()

mu_filenames = [] #存放變異體的檔案名稱
for i,item in enumerate(mutations): #產生變異體檔案出來
    filename = "test_" + str(i+1) + ".py"
    mu_filenames.append(filename)
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(item + "\n" + AssertPart)

import subprocess
output = []
for mus in mu_filenames: #執行shell
    # if mus == 'test_1.py':
    #     continue
    cmd = "pytest " + mus #要有空格==> pytest mus
    #shell set True can run
    output.append(subprocess.run([cmd], capture_output=True, shell=True).stdout.decode())
#對output list內的每組字串以\n分割
beslipt_output = []

for item in output:
    beslipt_output.append(item.split('\n'))
# with open('data.txt','w',encoding='UTF-8') as file:
#     for one in beslipt_output:
#         for two in  one:
#             file.write(two+'\n')

# for i in beslipt_output:
#     print(i,'')
    # for j in i:
    #     print(j,'')
# print(beslipt_output[1])
# 計算kill百分比 顯示沒有kill的字串

temp = killpercent(beslipt_output)

print(temp)