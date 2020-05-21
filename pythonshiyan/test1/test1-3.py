str1 = input("Please enter an English sentence: ")
str1 = str1.replace('!', ' ')
str1 = str1.replace(',', ' ')
str1 = str1.replace('.', ' ')
str1 = str1.replace('\'', ' ')
str1 = str1.replace('\"', ' ')
str1 = str1.lower()
print (str1)
list1 = str1.split()
#print(list1)
result = {}


for i in list1:
    num = i.strip()
    result[num] = result.get(num,0) + 1

print(result)
