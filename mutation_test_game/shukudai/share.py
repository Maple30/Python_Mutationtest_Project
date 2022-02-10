# 取小數點第n位
def get_two_float(f_str, n):
    f_str = str(f_str)
    a, b, c = f_str.partition('.')
    c = (c+"0"*n)[:n]       # 補0
    return ".".join([a, c])

# 輸出字串處理
def output_str_hadler(totalprograms, Killper, suvived, kill_status_record):
    output_string = []
    output_string.append('Total programs:' + str(totalprograms))
    output_string.append('Killpercentage:' + str(Killper) + '%')
    output_string.append('Total suvived programs:' + str(len(suvived)))
    
    for item in suvived:
        output_string.append(item[0])
        output_string.append("suvived functions:")
        for fucname in item[1:-1]:
            output_string.append(fucname)
        output_string.append("\n"+item[-1])
        output_string.append("")
    # print('i am output_str_hadler','')
    # print(output_string)
    return output_string, Killper, kill_status_record

# 計算kill比率並回傳輸出結果
def killpercent(beslipt_output=list(), assert_all_fun = []):
    total = len(beslipt_output)
    killed_counter = 0
    kill_status_record = []
    suvived = []
        # with open(i[0], 'r', encoding='UTF-8') as file:
    # print(beslipt_output)
    for one in beslipt_output:
        print(one)
        if "passed" in one[-2] and "failed" in one[-2]: #字串存在"passed"和"failed"
            for p,item in enumerate(one):
                if "short test summary info" in item:
                    killedfunc = []
                    suvived.append([one[p+1].split("::")[0].split(" ")[1]])
                    # 是Testclass的情況
                    if "Testclass" in one[p+1]:
                        for killedstest in one[p+1:-2]:
                            killedfunc.append(killedstest.split("::")[2].split(" ")[0])
                    # 非Testclass的情況
                    else:
                        for killedstest in one[p+1:-2]:
                            killedfunc.append(killedstest.split("::")[1].split(" ")[0])
                    
                    for IsTestFucName in one:
                        if "def" in IsTestFucName and "test" in IsTestFucName:
                            suvived[-1].append(IsTestFucName.split(" ")[-1][0:-1])
            # 紀錄有killed掉
            kill_status_record.append(True)
        elif ("failed" in one[-2]) and ("passed" not in one[-2]): #字串只存在"failed"而不存在"passed"
            killed_counter += 1
            # 紀錄有killed掉
            kill_status_record.append(True)
        else: # ("failed" not in one[-2]) and ("passed" in one[-2]) 只有passed存在
            for p,item in enumerate(one):
                if "[100%]" in item:
                    print(item)
                    suvived.append([item.split()[0]])
                    
                    # 將所有function name放入
                    for funName in assert_all_fun:
                        suvived[-1].append(funName)
            # 紀錄有killed失敗
            kill_status_record.append(False)

    # print("bslipt_output = ")
    # print(beslipt_output)
    # print("total = " + str(total))
    # print(suvived)
    for i in suvived:
        with open(i[0], 'r', encoding='UTF-8') as file:
            i.append(file.read())
            i[0] = i[0].split("/")[-1]
    # print(killed_counter,total)
    return output_str_hadler(total, get_two_float((killed_counter/total)*100,2), suvived, kill_status_record)
