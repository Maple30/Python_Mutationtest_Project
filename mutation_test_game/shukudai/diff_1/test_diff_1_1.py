def game(x):
    p=0
    if x >= 10:
        return 1
    elif (x+20) > 10:
        return 2
    if x < 10:
        return 3
    return p
def test_game():
    assert game(10)==2
    assert game(-10)==3
    assert game(12)==1
    