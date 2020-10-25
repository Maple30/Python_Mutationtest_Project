



def minima(Num1, Num2):  
    if Num1 > Num2:   
        return Num2
    else:
        return Num1
assert(10,minima(10,20))

def minima(Num1, Num2):
    if Num1 >= Num2:
        return Num2
    else:
        return Num1


assert(10,minima(10,20))
assert(8,minima(10,8))
assert(-100,minima(-100,20))
assert(0,minima(10,0))




def minima(Num1, Num2):
    if Num1 <= Num2:
        return Num2
    else:
        return Num1
assert(10,minima(10,20))


