def game(x):
    p=0
    if x > 10:
        return 1
    elif (x-1) > 8:
        return 2
    elif (x-3) < 0:
        return 3
    elif (x-5) < -10:
        return 4
    elif x < -20:
        return 5
    
    return p
def test_game():
    assert game(-2)==0
    assert game(10)==2
    assert game(9)==0
    assert game(8)==0
    assert game(-3)==0
    