def game(x):
    p=0
    if x == 50:
        return 1
    if x > 10:
        return 2
    elif (x-1) > 8:
        return 3
    elif (x+3) < 0:
        return 4

    return p

def test_game():
    assert game(99)==1
    assert game(0)==0
    assert game(2)==0
    assert game(-100)==4
    