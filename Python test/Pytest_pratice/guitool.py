import tkinter as tk
from tkinter import filedialog
from mutation import *

window = tk.Tk()
window.geometry("500x300")
def open_file():
    filename = filedialog.askopenfilename(title='開啟txt檔案', filetypes=[('txt', '*.py')])
    entry_filename.insert('insert', filename)
def print_suvived_file_kill_rate():
    filename = entry_filename.get()  #用get提取entry中的內容
    output_string = mutationtest(filename)
    mutation_output.set(output_string)

# 設定button按鈕接受功能
button_import = tk.Button(window, text="匯入檔案", command=open_file).pack()
# 設定entry
entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
entry_filename.pack()
# 嘗試輸出

mutation_output = tk.StringVar()    # 將label標籤的內容設定為字元型別，用var來接收hit_me函式的傳出內容用以顯示在標籤上
l = tk.Label(window, textvariable=mutation_output, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 說明： bg為背景，fg為字型顏色，font為字型，width為長，height為高
l.pack()

tk.Button(window, text="輸出", command=print_suvived_file_kill_rate).pack()

window.mainloop()
# 運行主程式