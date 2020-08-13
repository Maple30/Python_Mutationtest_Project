import os
from functions import *
def mutationtest(assert_program_filename="", mutate_program_filename="",options=[]):
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
            return ['No symbol can be mutate']

    AssertPart = "" ##讀入assert code 進行改寫
    
    with open(assert_program_filename,'r',encoding="UTF-8") as file:
        AssertPart = file.read()
        assert_all_fun = []
        temp = AssertPart.split('\n')
        for i in temp:
            if i.split(" ")[0] == "def" and "test_" in i.split(" ")[1]:
                assert_all_fun.append(i.split(" ")[1][0:-1])
    print(assert_all_fun)
    mu_filenames = [] #存放變異體的檔案名稱
    for i,item in enumerate(mutations): #產生變異體檔案出來
        filename = "test_" + str(i+1) + ".py"
        mu_filenames.append(filename)
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write(item + "\n" + AssertPart)

    import subprocess
    output = []
    for mus in mu_filenames: #執行shell
        cmd = "pytest " + mus #要有空格==> pytest mus
        #shell set True can run
        output.append(subprocess.run([cmd], capture_output=True, shell=True).stdout.decode())
    #對output list內的每組字串以\n分割
    beslipt_output = []

    for item in output:
        beslipt_output.append(item.split('\n'))
    # for i in beslipt_output:
    #     for j in i:
    #         print(j)
    output_string = killpercent(beslipt_output, assert_all_fun)

    return output_string