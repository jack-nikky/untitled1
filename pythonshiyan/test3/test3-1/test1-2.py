fileData = open("data.txt", mode="r")

dataList = fileData.read().split(",")


for i in range(100):
    dataList[i] = int(dataList[i])

dataList.sort()

# 转换成字符串
for i in range(100):
    dataList[i] = str(dataList[i])+','

#将新的数据写入一个文件中
newFile = open("data_asc.txt", mode="w+")
newFile.writelines(dataList)

fileData.close()
newFile.close()
