from time import time

from python.UserDatabase import Database
from python.model.User import User
from python.cryptography import *

menu = """1)Get user by username
2)Add User
3)Get user count"""
myDb = Database()

donguKontrol = True
while donguKontrol:
    print(menu)
    selection = int(input("Selection: "))
    
    if (selection == 1):
        username = input("Username: ")
        returnValue = myDb.getUserWithUsername(username=username)
        print(returnValue)
        
    elif (selection == 2):
        username = input("Username: ")
        password = input("Password: ")
        password = toMD5(password)
        email = input("Email: ")
        user_type = 1
        created_at = time()
        user = User(
            username=username,
            password=password,
            email=email,
            user_type=user_type,
            last_login=0,
            created_at=created_at
        )
        if (myDb.addUserIfNotExists(user)):
            print("User added")
        else:
            print("User already exists")
            
    elif (selection == 3):
        print(f"{myDb.getUserCount()} users.")
            