# from threefive import T35,T69
# class TestClass:
#     def test_ans35(self):
#         assert T35() == "no"
#     def test_ans69(self):
#         assert T69() == "yes"
import sys
#filename = str(sys.argv[2])
T = __import__("threefive")
class TestClass:
    def test_ans35(self):
        assert T.T35() == "no"
    def test_ans69(self):
        assert T.T69() == "yes"