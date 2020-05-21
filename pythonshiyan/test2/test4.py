def sign_up():  #注册

    username = input("Please create your name:")
    passwd = input("Please input your password:")
    if username not in user_dict.keys():
        user_dict[username] = passwd
        print(username, " successfully sign up!")
        choose = int(input("print 1 to sign in!"))
        if choose == 1:
            sign_in()
        elif choose == 0:
            sign_up()

    else:
        print("your username already exists, please input again")
        sign_up()

def sign_in():  #登录
    username = input("Please input your name:")
    passwd = input("Please input your password:")
    if username in user_dict.keys():
        if user_dict[username] == passwd:
            print(username, " successfully sign in!")
        elif user_dict[username] != passwd:  # 第一次失败
            passwd = input("Wrong password, Please input again:")
            if user_dict[username] == passwd:
                print(username, " successfully sign in!")
            elif user_dict[username] != passwd:  # 第二次失败
                passwd = input("Wrong password, Please input again:")
                if user_dict[username] == passwd:
                    print(username, " successfully sign in!")
                elif user_dict[username] != passwd:  # 第三次失败
                    print("Bye - bye")
    else:
        print("username no exists, Please input again")
        sign_in()

user_dict = {}   #用户信息字典

choose = int(input("sign up or sign in ? Please input 0 or 1:"))
while(True):

    if choose == 0:
        sign_up()
        exit()

    elif choose == 1:
        sign_in()
        exit()

    else:
        choose =int(input("Wrong command, please input again:"))








