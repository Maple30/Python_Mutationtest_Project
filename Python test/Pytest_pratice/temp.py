import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# window = tk.Tk()
# window.geometry("300x300")
# def get_value():
#     print(chkValue.get())

# chkValue = tk.BooleanVar() 
# chkValue.set(True)
 
# chkExample = tk.Checkbutton(window, text='Check Box', var=chkValue)
# chkExample.grid(column=0, row=0)
# tk.Button(window, text="print", command=get_value).grid(column=0,row=3,sticky='ew')

# window.mainloop()
# 運行主程式
AssertPart1 = []


with open("threefive.py",'r',encoding="UTF-8") as file:
    temp = file.readline()
    print(temp)
    while temp is not None and temp != "":
        temp = file.readline()
        for i in temp:
            if i == " ":
                pass
            elif i == "#":
                break
            else:
                AssertPart1.append(temp)
                break

        # print(temp)
for i in AssertPart1:
    print(i,end='')

# with open("threefive.py",'r',encoding="UTF-8") as file:
    
#     AssertPart2 = file.read()
# print(AssertPart2)

# Test = [9,1,2,9,4,5]


# for i,item in enumerate(Test):
#     if i == item:
# print(Test)