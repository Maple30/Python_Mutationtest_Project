import tkinter as tk
from tkinter import filedialog
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
window.geometry("300x300")

def open_file():
    filename = filedialog.askopenfilename(title='開啟txt檔案', filetypes=[('txt', '*.py')])
    entry_filename.delete()
    entry_filename.insert('insert', filename)


def print_suvived_file_kill_rate():
    filename = entry_filename.get()  #用get提取entry中的內容
    output_string = mutationtest(filename)
    # print(output_string)
    # mutation_output.set(output_string)
    for item in output_string:
        listbox.insert(tk.END, item)
    scrollbar.config(command=listbox.yview)
def clear_all_listbox():
    listbox.delete('0',tk.END)

# 設定button按鈕接受功能
button_import = tk.Button(window, text="import file", command=open_file).grid(column=2,row=0,sticky='w')
# 設定entry
entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
entry_filename.grid(column=0,row=0,columnspan=2)
# 嘗試輸出

tk.Button(window, text="output", command=print_suvived_file_kill_rate).grid(column=0,row=2,sticky='ew')
tk.Button(window, text="clear", command=clear_all_listbox).grid(column=1,row=2,sticky='ew')
global scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=1,column=2,sticky="nsw")

global listbox
listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
listbox.grid(column=0,row=1,columnspan=2,sticky='nsew')
listbox.insert(tk.END, 'mutation test result:')
scrollbar.config(command=listbox.yview)

window.mainloop()
# 運行主程式