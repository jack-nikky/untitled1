def dateTwoDaysLater(month, day, year):
    M1 = {4, 6, 9, 11}
    M2 = {1, 3, 5, 7, 8, 10}
    M3 = {12}
    M4 = {2}

    D1 = set(list(range(1, 27)))
    D2 = {27}
    D3 = {28}
    D4 = {29}
    D5 = {30}
    D6 = {31}

    state = 0  #state表示是否是闰年，0表示不是，1表示是闰年
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        state = 1

    if month in M1 and day in D1 | D2 | D3:
        day = day + 2
    elif month in M1 and day in D4:
        day = 1
        month = month + 1
    elif month in M1 and day in D5:
        day = 2
        month = month + 1
    elif month in M2 and day in D1 | D2 | D3 | D4:
        day = day + 2
    elif month in M2 and day in D5:
        day = 1
        month = month  + 1
    elif month in M2 and day in D6:
        day = 2
        month = month + 1
    elif month in M3 and day in D1 | D2 | D3 | D4:
        day = day + 2
    elif month in M3 and day in D5:
        day = 1
        month = 1
        year = year + 1
    elif month in M3 and day in D6:
        day = 2
        month = 1
        year = year +1
    elif month in M4 and day in D1:
        day = day + 2
    elif month in M4 and day in D2 and state == 1:
        day = day + 2
    elif month in M4 and day in D2 and state == 0:
        day = 1
        month = month + 1
    elif month in M4 and day in D3 and state == 1:
        day = 1
        month = month + 1
    elif month in M4 and day in D3 and state == 0:
        day=2
        month = month + 1
    elif month in M4 and day in D4 and state == 1:
        day = 2
        month = month + 1
    else:
        return "输入错误"

    return "{}年{}月{}日".format(year, month, day)


testlist = [[1, 4, 27, 2005, "2005年4月29日"],
            [2, 4, 29, 2005, "2005年5月1日"],
            [3, 6, 30, 2000, "2000年7月2日"],
            [4, 6, 31, 2000, "输入错误"],
            [5, 3, 29, 2005, "2005年3月31日"],
            [6, 5, 30, 2005, "2005年6月1日"],
            [7, 5, 31, 2005, "2005年6月2日"],
            [8, 12, 20, 2005, "2005年12月22日"],
            [9, 12, 30, 2000, "2001年1月1日"],
            [10, 12, 31, 2000, "2001年1月2日"],
            [11, 2, 26, 2000, "2000年2月28日"],
            [12, 2, 27, 2000, "2000年2月29日"],
            [13, 2, 27, 2005, "2005年3月1日"],
            [14, 2, 28, 2000, "2000年3月1日"],
            [15, 2, 28, 2005, "2005年3月2日"],
            [16, 2, 29, 2000, "2000年3月2日"],
            [17, 2, 29, 2005, "输入错误"],
            [18, 2, 31, 2000, "输入错误"]] #判定表测试用例

print("{:^12}{:^18}{:^18}{:^18}{:^18}".format("用例编号", "输入条件", "预期结果", "实际结果", "结论"))
for i in testlist:
    temp = dateTwoDaysLater(i[1], i[2], i[3])
    conclusion = "fail"
    if temp == i[4]:
        conclusion = "pass"
    print("{:^18d}{:^6}{:^6}{:^6}{:^18}{:^18}{:^18}".format(i[0], i[1], i[2], i[3], i[4], temp, conclusion))

