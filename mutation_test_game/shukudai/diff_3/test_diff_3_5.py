def game(x):
    p=0
    if x > 50:
        return 1
    if x > 10:
        return 2
    elif (x+1) > 8:
        return 3
    elif (x+3) < 0:
        return 4

    return p

def test_game():
    assert game(675)==1
    assert game(1234)==1
    assert game(876567546)==1
    assert game(345745675)==1
    assert game(57654567546)==1
    