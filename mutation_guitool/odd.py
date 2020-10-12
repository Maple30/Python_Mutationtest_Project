def odd(the_line_have_how_many_num):
    flag = 0
    i = 2
    while(1):
        flag = flag + 2*i-1
        if 2*i-1 == the_line_have_how_many_num:
            break
        i = i + 1
    the_last_num = 2*flag + 1
    print(the_last_num*3 - 6)

odd(3)
odd(5)
odd(7)
odd(17)
odd(33)
odd(99)
