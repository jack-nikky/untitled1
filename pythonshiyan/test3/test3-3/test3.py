# coding=gbk
import os


# 输出目录下的文件名及其文件的行数
def getNameAndLines(filePath, menuLines):
    for fileName in menuLines:
        count = 0
        f = open(filePath + "/" + fileName, "r",encoding='gbk')
        for line in f.readlines():
            count = count + 1
        f.close()
        print(fileName.strip(".txt") + ": " + str(count))

#第一行插入古诗名
def insertName(filePath, menuLines):
    for fileName in menuLines:
        f = open(filePath + "/" + fileName, "r",encoding='gbk')
        readLins = f.readlines()
        f.close()
        f1 = open(filePath + "/" + fileName, "w",encoding='gbk')
        f1.write(fileName.strip(".txt") + "\n")
        f1.writelines(readLins)
        f1.close()


filePath = "poem"
menuLines = []
for root, dirs, files in os.walk(filePath):
    menuLines = files

getNameAndLines(filePath, menuLines)
insertName(filePath, menuLines)
