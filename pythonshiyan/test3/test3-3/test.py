# coding=gbk
import os


# ���Ŀ¼�µ��ļ��������ļ�������
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
    # print(root) #��ǰĿ¼·��
    # print(dirs) #��ǰ·����������Ŀ¼
    menuLines = files
    # print(files) #��ǰ·�������з�Ŀ¼���ļ�

getNameAndLines(filePath, menuLines)
insertName(filePath, menuLines)
