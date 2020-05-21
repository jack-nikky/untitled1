import random

fileData = open("data.txt", mode="w+")

#随机生成随机数的一种形式
for i in range(0,100):
        # 生成100个1-1000之间随机整数写到文件中
    randData = str(random.randint(1,1000))
    realData = randData+","

    if(i==99):
        fileData.write(randData)
    else:
        fileData.write(realData)

fileData.close()


