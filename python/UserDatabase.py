
from os import getcwd
import sqlite3 as sql # sqlite3 is a module

from python.model.User import User

CREATETABLE_USER = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    user_type INTEGER,
    last_login INTEGER,
    created_at INTEGER
    );"""

class Database():
    dbName = "users.db"
    dbLoc = fr"db/{dbName}"
    
    def __init__(self) -> None:
        self.createDB()
    

    def createDB(self):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(CREATETABLE_USER)
        self.db.commit()
        self.db.close()


    def addUser(self,user:User):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        KEY = f"name,surname,username,password,email,user_type,last_login,created_at"
        VALUES = f"""
        '{user.getName()}',
        '{user.getSurname()}',
        '{user.getUsername()}',
        '{user.getPassword()}',
        '{user.getEmail()}',
        {user.getUserType()},
        {user.getLastLogin()},
        {user.getCreatedAt()}
        """
        self.im.execute(f"INSERT INTO users ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        self.db.close()

    def addUserIfNotExists(self,user:User):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM users WHERE username = '{user.getUsername()}'")
        result = self.im.fetchone()
        if result != None:
            return False
        self.addUser(user)
        self.db.close()
        return True
    
    def getUserWithUsername(self, username:str) -> User:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM users WHERE username = '{username}'")
        result = self.im.fetchone()
        print(result)
        if result == None:
            return None
        user = User()
        user.setID(result[0])
        user.setName(result[1])
        user.setSurname(result[2])
        user.setUsername(result[3])
        user.setPassword(result[4])
        user.setEmail(result[5])
        user.setUserType(result[6])
        user.setLastLogin(result[7])
        user.setCreatedAt(result[8])
        self.db.close()
        return user
        
    def getUserCount(self) -> int:
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
        self.im.execute("SELECT COUNT(*) FROM users")
        result = self.im.fetchone()
        self.db.close()
        return result[0]
    

    
    

    