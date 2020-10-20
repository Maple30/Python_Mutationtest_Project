def game(x):
    p=0
    if x > 10:
        return 1
    elif (x/1) > 8:
        return 2
    elif (x+3) < 0:
        return 3
    elif (x-40) < -10:
        return 4
    elif x < -20:
        return 5
    
    return p
def test_game():
    assert game(2)==4
    assert game(10)==2
    assert game(9)==4
    assert game(8)==4
    