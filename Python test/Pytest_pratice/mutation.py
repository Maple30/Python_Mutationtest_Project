import os
from functions import *
def mutationtest(assert_program_filename=""):
    mutations = [] #存放變異體
    with open('threefive.py', 'r', encoding='UTF-8') as file:
        origin = file.read() #讀入要做測試的程式
        
        mutations += relation_symbols_check(origin)# relation_symbols
        mutations += opration_symbols_check(origin)#opration_symbols
        mutations += logic_symbols_check(origin)# logic_symbols
        mutations += binary_symbols_check(origin)# binary_symbols

    AssertPart = "" ##讀入assert code 進行改寫
    
    with open(assert_program_filename,'r',encoding="UTF-8") as file:
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
    #     for j in i:
    #         print(j,'')
    # print(beslipt_output[1])
    # 計算kill百分比 顯示沒有kill的字串

    Killper, suvived = killpercent(beslipt_output)
    
    output_string = []
    output_string.append('Killpercentage:' + str(Killper))
    output_string.append('Total suvived programs:'+str(len(suvived)))
    for item in suvived:
        output_string.append(item)
    # print(output_string)
    return output_string
    ## python gui tool
    # import tkinter as tk
    # from tkinter import filedialog

    # window = tk.Tk()
    # window.geometry("500x300")
    # def open_file():
    #     filename = filedialog.askopenfilename(title='開啟txt檔案', filetypes=[('txt', '*.py')])
    #     entry_filename.insert('insert', filename)
        
    # # 設定button按鈕接受功能
    # button_import = tk.Button(window, text="匯入檔案", command=open_file).pack()
    # # 設定entry
    # entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
    # entry_filename.pack()
    # # 嘗試輸出
    # def print_file():
    #     a = entry_filename.get()  #用get提取entry中的內容
    #     print(a)
    # tk.Button(window, text="輸出", command=print_file).pack()



    # window.mainloop()
    # # 運行主程式