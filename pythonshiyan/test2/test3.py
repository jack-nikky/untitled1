import random

listhistory = {}
for i in range(0,10):
    username = "user"+str(i)
    set_film = set()
    for j in range(random.randint(1,10)):
        filmname = "film" + str(random.randint(1,10))
        set_film.add(filmname)
    listhistory[username] = set_film
print("历史数据")
for i,j in listhistory.items():  #历史数据输出
    print(i, ":", j)

#待测用户曾经看过并感觉不错的电影
user = {'film1', 'film2', 'film3'}
print("待测用户\n user:",user)

similar_user = ""   #相似用户
similarity = 0  #相似度

for i,j in listhistory.items():
    if len(j&user) > similarity:
        similarity = len(j&user)
        similar_user = i

print("和你最想似的用户是：",similar_user)
print("Ta最喜欢看滴的电影是：",listhistory[similar_user])
print("Ta看过的电影中你还没看过的有：",listhistory[similar_user]-user)