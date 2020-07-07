boolean_symbols = (">","<",">=","<=","==","!=") #布林運算符號
Test = ("b","c")
Testlist = list(boolean_symbols)
Testlist2 = list(Test)
Testlist += Testlist2
print(Testlist)