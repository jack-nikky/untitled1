def typeTriangle(a, b, c):
    if a == 1000 or b == 1000 or c == 1000:
        return "提示：请输入数据"
    elif a <= 0 or a > 100 or b <= 0 or b > 100 or c <= 0 or c > 100 or isinstance(a, int)==False or isinstance(b, int)==False or isinstance(c, int)==False:
        return "提示：输入不符合要求"
    elif a + b <= c or b + c <= a or a + c <= b:
        return "非三角形"
    elif a == b and b == c:
        return "等边三角形"
    elif a == b or b == c or a == c:
        return "等腰三角形"
    else:
        return "一般三角形"

list2 = [[1, 2, 1000, 1000, "提示：请输入数据"],
         [2, 101, 3, 3, "提示：输入不符合要求"],
         [3, 1, 2, 5, "非三角形"],
         [4, 3, 3, 3, "等边三角形"],
         [5, 2, 2, 3, "等腰三角形"],
         [6, 5, 6, 10, "一般三角形"]]  #路径测试用例，其中1000表示没输入

print("{:^12}{:^18}{:^18}{:^18}{:^18}".format("用例编号", "输入条件", "预期结果", "实际结果", "结论"))
for i in list2:
    temp = typeTriangle(i[1], i[2], i[3])
    conclusion = "fail"

    for j in range(len(i)):
        if i[j] == 1000:
            i[j] = "-"

    if temp == i[4]:
        conclusion = "pass"
    print("{:<18d}{:<6}{:<6}{:<6}{:<25}{:<25}{:<18}".format(i[0], i[1], i[2], i[3], i[4], temp, conclusion))
