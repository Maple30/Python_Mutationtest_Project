import sys, pytest

def test_game():
    assert game(3,10) == 2
    assert game(10,0) == 10
    assert game(10,1) == 1