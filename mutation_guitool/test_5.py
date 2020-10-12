def game(Num):
    Num = int(Num)
    for i in range(1,Num+1):
        digit_sum = 0
        
        Num_string = str(i)
        for j in range(len(Num_string)):
            digit_sum = digit_sum + int(Num_string[j])
        digit_sum = digit_sum + i

        if digit_sum != Num:
            return i
    return 0
import sys, pytest

def test_game():
    assert game("216")==198
    assert game("121")==0
    assert game("2005")==1979
    assert game("1") == 0