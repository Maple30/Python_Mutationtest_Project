import os

from functions import *

mutate_program_filename = "NetGame.py"
options=[True,False,False,False]

mutations = [] #存放變異體
with open(mutate_program_filename, 'r', encoding='UTF-8') as file:
    temp = file.readline() #讀入要做測試的程式
    origin = ""
    origin += temp
    while temp is not None and temp != "":
        temp = file.readline()
        for i in temp:
            if i == " ":
                pass
            elif i == "#":
                break
            else:
                origin += temp
                break
    if options[0] == True:
        mutations += relation_symbols_check(origin)# relation_symbols
    if options[1] == True:
        mutations += opration_symbols_check(origin)#opration_symbols
    if options[2] == True:
        mutations += logic_symbols_check(origin)# logic_symbols
    if options[3] == True:
        mutations += binary_symbols_check(origin)# binary_symbols
    try:
        mutations[0]
    except IndexError as e:
        printf('No symbol can be mutate')

AssertPart = "" #讀入assert code 進行改寫

mu_filenames = [] #存放變異體的檔案名稱
for i,item in enumerate(mutations): #產生變異體檔案出來
    filename = "test_" + str(i+1) + ".py"
    mu_filenames.append(filename)
    with open("../"+filename, 'w', encoding="UTF-8") as file:
        file.write(item + "\n" + AssertPart)