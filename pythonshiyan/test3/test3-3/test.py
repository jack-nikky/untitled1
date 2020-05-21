# coding=gbk
import os


# 输出目录下的文件名及其文件的行数
def getNameAndLines(filePath, menuLines):
    for fileName in menuLines:
        count = 0
        f = open(filePath + "/" + fileName, "r")
        for line in f.readlines():
            count = count + 1
        f.close()
        print(fileName.strip(".txt") + ": " + str(count))


def insertName(filePath, menuLines):
    for fileName in menuLines:
        f = open(filePath + "/" + fileName, "r")
        readLins = f.readlines()
        f.close()
        f1 = open(filePath + "/" + fileName, "w")
        f1.write(fileName.strip(".txt") + "\n")
        f1.writelines(readLins)
        f1.close()


filePath = "poem"
menuLines = []
for root, dirs, files in os.walk(filePath):
    # print(root) #当前目录路径
    # print(dirs) #当前路径下所有子目录
    menuLines = files
    # print(files) #当前路径下所有非目录子文件

getNameAndLines(filePath, menuLines)
insertName(filePath, menuLines)
