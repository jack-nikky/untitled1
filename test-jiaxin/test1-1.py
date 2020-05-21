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





list1 = [[1, 50, 50, 1, "等腰三角形"],
         [2, 50, 50, 2, "等腰三角形"],
         [3, 50, 50, 50, "等边三角形"],
         [4, 50, 50, 99, "等腰三角形"],
         [5, 50, 50, 100, "非三角形"],
         [6, 50, 1, 50, "等腰三角形"],
         [7, 50, 2, 50, "等腰三角形"],
         [8, 50, 99, 50, "等腰三角形"],
         [9, 50, 100, 50, "非三角形"],
         [10, 1, 50, 50, "等腰三角形"],
         [11, 2, 50, 50, "等腰三角形"],
         [12, 99, 50, 50, "等腰三角形"],
         [13, 100, 50, 50, "非三角形"]]
print("{:^7}{:^12}{:^12}{:^12}{:^12}".format("用例编号", "输入条件", "预期结果", "实际结果", "结论"))
for i in list1:
    temp = typeTriangle(i[1], i[2], i[3])
    conclusion = "fail"
    if temp == i[4]:
        conclusion = "pass"
    print("{:^12d}{:^4d}{:^4d}{:^4d}{:^12}{:^12}{:^12}".format(i[0], i[1], i[2], i[3], i[4], temp, conclusion))


