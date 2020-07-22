# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from mutation import *

# window = tk.Tk()
# window.geometry("500x300")
# def open_file():
#     filename = filedialog.askopenfilename(title='開啟txt檔案', filetypes=[('txt', '*.py')])
#     entry_filename.insert('insert', filename)
# def print_suvived_file_kill_rate():
#     filename = entry_filename.get()  #用get提取entry中的內容
#     output_string = mutationtest(filename)
#     # mutation_output.set(output_string)
#     # for item in (1,20):
#     #     listbox.insert(tk.END, item)
#     # listbox.pack(side=tk.LEFT, fill=tk.BOTH)
#     # scrollbar.config(command=listbox.yview)

# # 設定button按鈕接受功能
# button_import = tk.Button(window, text="import file", command=open_file).pack()
# # 設定entry
# entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
# entry_filename.pack()
# # 嘗試輸出

# tk.Button(window, text="output", command=print_suvived_file_kill_rate).pack()

# global scrollbar
# scrollbar = tk.Scrollbar(window)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# global listbox
# listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)


# window.mainloop()
# # 運行主程式

window = tk.Tk()
window.geometry("350x300")

#開啟驗證檔
def open_assert_file():
    filename = filedialog.askopenfilename(title='開啟py檔案', filetypes=[('py', '*.py')])
    try: 
        entry_assert_filename.delete(0,'end') #刪除才不會有多有個檔名
    except TypeError:
        print("nothing")
    entry_assert_filename.insert('insert', filename)

#開啟變異檔
def open_mutate_file():
    filename = filedialog.askopenfilename(title='開啟py檔案', filetypes=[('py', '*.py')])
    try: 
        entry_mutate_filename.delete(0,'end') #刪除才不會有多有個檔名
    except TypeError:
        print("nothing")
    entry_mutate_filename.insert('insert', filename)

def print_suvived_file_kill_rate():
    assert_filename = entry_assert_filename.get()  #用get提取entry中的內容
    mutate_filename = entry_mutate_filename.get()
    # print(assert_filename)
    # (relation, opration, logic)
    options = [relation_symbols_chkValue.get(),opration_symbols_chkValue.get(),logic_symbols_chkValue.get(),binary_symbols_chkValue.get()]
    if True not in options:
        r=mb.showinfo("error", "No options", detail="No options")
        return 0
    elif assert_filename == '' or mutate_filename == '':
        r=mb.showinfo("error", "No file", detail="No file")
        return 0
    output_string = mutationtest(assert_filename, mutate_filename, options)

    for item in output_string:
        listbox.insert(tk.END, item)
    scrollbar.config(command=listbox.yview)
def clear_all_listbox():
    listbox.delete('0',tk.END)

# 設定button按鈕接受功能
button_import = tk.Button(window, text="import assert file", command=open_assert_file).grid(column=2,row=0,sticky='w')
button_import = tk.Button(window, text="import tested file", command=open_mutate_file).grid(column=2,row=1,sticky='w')
# 設定要做變異測試的檔案及assert程式的檔案 entry
entry_assert_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
entry_assert_filename.grid(column=0,row=0,columnspan=2)
entry_mutate_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
entry_mutate_filename.grid(column=0,row=1,columnspan=2)

entry_assert_filename.insert('insert', "/mnt/c/Users/st096/Desktop/Python_Test_Project/Python test/Pytest_pratice/test_assert.py")
entry_mutate_filename.insert('insert', "/mnt/c/Users/st096/Desktop/Python_Test_Project/Python test/Pytest_pratice/threefive.py")
# entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
# entry_filename.grid(column=0,row=0,columnspan=2)
# 嘗試輸出

tk.Button(window, text="output", command=print_suvived_file_kill_rate).grid(column=0,row=5,sticky='ew')
tk.Button(window, text="clear", command=clear_all_listbox).grid(column=1,row=5,sticky='ew')

# 輪軸
global scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(column=2,row=2,sticky="nsw")

# 輸出結果(kill per, suvived program's name)
global listbox
listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
listbox.grid(column=0,row=2,columnspan=2,sticky='nsew')
listbox.insert(tk.END, 'mutation test result:')
scrollbar.config(command=listbox.yview)

# 變異選項
relation_symbols_chkValue = tk.BooleanVar()
relation_symbols_chkValue.set(True)
opration_symbols_chkValue = tk.BooleanVar()
opration_symbols_chkValue.set(False)
logic_symbols_chkValue = tk.BooleanVar()
logic_symbols_chkValue.set(False)
binary_symbols_chkValue = tk.BooleanVar()
binary_symbols_chkValue.set(False)


relation_symbols_chk = tk.Checkbutton(window, text='relation_symbols', var=relation_symbols_chkValue)
relation_symbols_chk.grid(column=0, row=3)
opration_symbols_chk = tk.Checkbutton(window, text='opration_symbols', var=opration_symbols_chkValue)
opration_symbols_chk.grid(column=1, row=3)
logic_symbols_chk = tk.Checkbutton(window, text='logic_symbols', var=logic_symbols_chkValue)
logic_symbols_chk.grid(column=2, row=3)
binary_symbols_chk = tk.Checkbutton(window, text='binary_symbols', var=binary_symbols_chkValue)
binary_symbols_chk.grid(column=0, row=4)
window.mainloop()
# 運行主程式