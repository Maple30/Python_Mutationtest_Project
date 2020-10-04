def test_game(Ascending_power_Num):
    Descending_power_Num = 0
    Appeared_Num = []
    New_num = 0

    while(1):
        Ascending_power_Num = list(map(int,Ascending_power_Num))
        Ascending_power_Num.sort(reverse=True)
        Descending_power_Num = sorted(Ascending_power_Num)

        New_num = int("".join([str(X) for X in Ascending_power_Num])) / int("".join([str(Y) for Y in Descending_power_Num]))
        New_num = str(New_num)
        Ascending_power_Num = New_num

        if New_num in Appeared_Num:
            return len(Appeared_Num) + 1
        else:
            Appeared_Num.append(New_num)
            Ascending_power_Num = New_num
