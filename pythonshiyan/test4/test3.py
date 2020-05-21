str1 = input("Please input the String:\n")
list1 = []

list2 = str1.split()
for i in list2:
    try:
        i = float(i)
        list1.append(i)
    except:
        pass

for i in list1:
    print("数字：",i)
print("合法的数字一个有{}个".format(len(list1)))
