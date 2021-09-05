import json, os

authAdmin = 'D:\loginAdmin.json' #your directory

os.system('cls')
with open(authAdmin, 'r') as json_file:
    users = json.load(json_file) #users variable to read all the row in your json file

x = True #declaration of condition loop
while x:
    os.system('cls')
    print("input 0 to back")
    username = input("Username : ")
    password = input("Password : ")

    #load and check all the values in json file (1 by 1)
    for user in users:
        if username == user['username'] and password == user['password']: #condition if the value correct
            os.system('cls')
            input(f"\n\n{'Hello, '+user['username']+'!':^40}")
            #login successful (do what you want)
            while x:
                os.system('cls')
                print("[1] Menu One")
                print("[2] Menu Two")
                print("[3] Logout")
                inputUser = int(input("Choose : "))
                if inputUser == 1:
                    print("this is menu 1")
                elif inputUser == 2:
                    print('this is menu 2')
                elif inputUser == 3: 
                    print("Log out as admin") 
                    #to log out you just need to change the variable condition (x) to False
                    x = False
                else:
                    print("False input")

        elif username == "0" and password == "0": #condition if you want to back
            os.system('cls')
            x = False
            break
        
    else: #if username or password is false
        input("Invalid username/password, press Enter to input again")