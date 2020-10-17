def game(Ascending_power_Num):
        #降冪數列
    #升冪數列
    Descending_power_Num = 0
    Appeared_Num = []
    # New_num存放相減出來的新數字
    New_num = 0

    while(1):
        # 轉乘int list 用降冪排列
        Ascending_power_Num = list(map(int,Ascending_power_Num))
        Ascending_power_Num.sort(reverse=True)
        # 轉為升冪
        Descending_power_Num = sorted(Ascending_power_Num)
        # New_num存放相減出來的新數字
        New_num = int("".join([str(X) for X in Ascending_power_Num])) - int("".join([str(Y) for Y in Descending_power_Num]))
        New_num = str(New_num)
        Ascending_power_Num = New_num
        # 確認是否出現過了
        if New_num in Appeared_Num:
            return len(Appeared_Num) + 1
        else:
            #加入出現過數字的列表裡
            Appeared_Num.append(New_num)
            #新的降冪
            Ascending_power_Num = New_num
        

AAA = ["123456789", "1234", "444", "1", "2", "4", "16", "39", "65", "3616", "10262"]
for i in AAA:
    print("Original number was {ggg}".format(ggg=i))
    print("Chain length {AA}".format(AA=game(i)))
    # game("1234")
# print(game("1234"))
