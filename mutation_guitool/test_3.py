def game(Num):
    if Num <= 5 or Num < 10000:
        return "yes"
    return "no"
import sys, pytest

def test_game():
    assert game(5)== "no"
    assert game(10)== "yes"
    assert game(15)== "yes"
    assert game(20)== "yes"
    