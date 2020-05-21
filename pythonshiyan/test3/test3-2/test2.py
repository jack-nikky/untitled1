def addWord():
    fileWord = open("Word.txt", 'r+')
    wordEnglish = input("请输入你要添加的单词：")
    dictWord = {}
    for line in fileWord.readlines():
        lineword = line.split()
        dictWord[lineword[0]] = lineword[1]

   # print(dictWord)

    if wordEnglish not in dictWord.keys():
        wordChinese = input("请输入该单词的中文释义（多个意思用英文逗号隔开):")
        wordInfo = [wordEnglish , " " , wordChinese,"\n"]
        fileWord.writelines(wordInfo)
        fileWord.close()
    else:
        print("该单词已存在于字典中\n")
        fileWord.close()


def findWord():
    word = input("请输入要查找的单词：")
    fileWord = open("Word.txt", 'r')  # 以只读模式打开
    dictWord = {}
    for line in fileWord.readlines():
        lineword = line.split()
        dictWord[lineword[0]] = lineword[1]
    fileWord.close()
    if word in dictWord.keys():
        print("该单词的释义为:", dictWord[word],"\n")

    else:
        print("字典库内未找到", word,"\n")


while(True):
    choose = input("请输入数字选择操作：\n 1-添加   2-查询   3-退出\n")
    if choose == '1':
        addWord()

    elif choose == '2':
        findWord()


    elif choose == '3':
        exit()

    else:
        print("输入有误 !!!!!!\n")

