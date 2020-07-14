import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# root = tk.Tk()

# b1 = ttk.Button(root, text='b1')
# b1.grid(row=0, column=0, sticky="w")

# e1 = ttk.Entry(root)
# e1.grid(row=0, column=1, sticky="ew")

# tree = ttk.Treeview(root)
# scroll = ttk.Scrollbar(root)
# scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.

# scroll.configure(command=tree.yview)
# tree.configure(yscrollcommand=scroll.set)

# # root.columnconfigure(0, weight=1) Removing this line fixes the sizing issue with the entry field.
# root.columnconfigure(1, weight=1)
# root.rowconfigure(1, weight=1)

# root.mainloop()


window = tk.Tk()
window.geometry("300x300")

def open_file():
    filename = filedialog.askopenfilename(title='開啟txt檔案', filetypes=[('txt', '*.py')])
    entry_filename.insert('insert', filename)
def print_suvived_file_kill_rate():
    filename = entry_filename.get()  #用get提取entry中的內容
    # output_string = mutationtest(filename)
    # mutation_output.set(output_string)
    for item in (1,20):
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