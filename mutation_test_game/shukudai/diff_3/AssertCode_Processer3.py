import sys
import subprocess
from NetGame import game
sys.path.append("/home/user777/Python_Mutationtest_Project/mutation_test_game/shukudai")
import share

#def 執行測試並回傳結果
def run(mu_filenames):
    print(mu_filenames)
    assert_all_fun = ["game(Ascending_power_Num)"]
    output = []
    for mus in mu_filenames: #執行shell
        cmd = "pytest " + "shukudai/diff_3/" + mus #要有空格==> pytest mus
        #shell set True can run
        output.append(subprocess.run([cmd], capture_output=True, shell=True).stdout.decode())
    # print()
    #對output list內的每組字串以\n分割
    beslipt_output = []
    for item in output:
        beslipt_output.append(item.split('\n'))
    # for i in beslipt_output:
    #     for j in i:
    #         print(j)
    output_string, killper, kill_status_record = share.killpercent(beslipt_output, assert_all_fun)

    return output_string, killper, kill_status_record

# assertcode產生
def AssertCode(input):
    As_Ans_Ar = []

    for i in range(len(input)):
        As_Ans_Ar.append(game(input[i]))
    
    As_string = "\ndef test_game():\n    "
    for i,ele in enumerate(As_Ans_Ar):
        As_string += "assert game({input1})=={ans}\n    ".format(
            input1 = str(input[i]),
            ans = ele
        )

    # print(As_string)

    mu_filenames =[]
    
    # 產生變異的題目
    pos = "//home/user777/Python_Mutationtest_Project/mutation_test_game/shukudai/diff_3/"
    for i in range(1,10):
        mu_filenames.append("test_diff_3_{num}.py".format(num=i))
        mutated = ""
        with open("test_{num}.py".format(num=i), 'r', encoding="UTF-8") as file:
            mutated = file.read() + As_string

        with open(pos + "test_diff_3_{num}.py".format(num=i), 'w', encoding="UTF-8") as file:
            file.write(mutated)

    return run(mu_filenames)
