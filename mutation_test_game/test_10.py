def T35():
    if 3 != 5:
        return "yes"
    else:
        return "no"
def T69():
    if 6+1 < 9:
        return "yes"
    else:
        return "no"


import sys, pytest
# class TestClass:
#     def test_ans35(self):
#         assert T35() == "no"
#     def test_ans69(self):
#         assert T69() == "no"

def test_ans35():
    assert T35() == "no"
def test_ans69():
    assert T69() == "no"