import sys, pytest

def test_game():
    assert game("216")==198
    assert game("121")==0
    assert game("2005")==1979
    assert game("1") == 0