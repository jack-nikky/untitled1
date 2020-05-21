import random

N = 1  # 用户输入的次数
num = random.randint(0, 100)
print("=========猜数游戏开始=========")
while True:
    try:
        my_num = int(input("请输入你猜测的数： "))
        # print("第{}次猜测".format(N))
        if my_num > num:
            print("遗憾，太大了")
        elif my_num < num:
            print("遗憾， 太小了")
        else:
            print("预测{}次，恭喜你猜中了".format(N))
            break

    except Exception as err:
        print("输入内容必须是整数")
    else:
        N = N + 1
