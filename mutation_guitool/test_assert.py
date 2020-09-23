import sys, pytest

def test_game():
    assert game("12234")==9
    assert game("214124")==17