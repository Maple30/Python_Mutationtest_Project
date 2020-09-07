import sys
from NetGame import game
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game")

def AssertCode(input):
    As_Ans_Ar = []
    # 先找出所有未變異前的答案
    for i in range(len(input)):
        As_Ans_Ar.append(game(input[i][0],input[i][1]))
    
    # 產生assertcode
    As_string = "def test_game():\n    "
    for i,ele in enumerate(As_Ans_Ar):
        As_string += "assert game({input1})={ans}\n    ".format(
            input1 = str(input[i][0]) + "," + str(input[i][1]),
            ans = ele
        )
    print(As_string)

    pos = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_1/"
    for i in range(1,4):
        mutated = ""
        with open("test_{num}.py".format(num=i), 'r', encoding="UTF-8") as file:
            mutated = file.read() + As_string
        with open(pos + "test_{num}.py".format(num=i), 'w', encoding="UTF-8") as file:
            file.write(mutated)