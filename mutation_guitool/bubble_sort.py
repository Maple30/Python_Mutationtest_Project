def game(x, y){
    p=0
    if (x>10 or y==1):
        return 1
    elif (x+y) > 10:
        return 2
    if y < 10:
        return 3
    return p
}