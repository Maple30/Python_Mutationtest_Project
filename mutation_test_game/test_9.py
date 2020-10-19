def game(x):
    p=0
    if x > 10:
        return 1
    elif (x-1) > 8:
        return 2
    elif (x+20) < 35:
        return 3
    elif (x-40) < -10:
        return 4
    elif x <= -20:
        return 5
    
    return p

