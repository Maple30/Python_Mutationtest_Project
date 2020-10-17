import sys, pytest

def test_game():
    assert game(5)== "no"
    assert game(10)== "yes"
    assert game(15)== "yes"
    assert game(20)== "yes"
    