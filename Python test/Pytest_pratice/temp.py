import tkinter as tk
def aaa():
    for i in range(20):
        listbox.insert(tk.END, str(i))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=listbox.yview)


master = tk.Tk()

button_import = tk.Button(master, text="匯入檔案", command=aaa).pack()
global scrollbar
scrollbar = tk.Scrollbar(master)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

global listbox
listbox = tk.Listbox(master, yscrollcommand=scrollbar.set)

master.mainloop()