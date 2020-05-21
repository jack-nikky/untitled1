import random

count1 = 0
count2 = 0


for i in range(10000):
    x = random.randint(1,3)
    y = random.randint(1,3)
    if x == y:
        count1 = count1 + 1
    else:count2 = count2 + 1

rate1 = "%.2f%%"%(count1/100)
rate2 = "%.2f%%"%(count2/100)
print("共进行10000次试验\n 不换门的胜率为{}\n 换门的胜率为{}".format(rate1,rate2))