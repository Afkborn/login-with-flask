
class User:
    def __init__(self,
                id : int = None,
                name : str = None,
                surname : str = None,
                username : str = None,
                password : str = None,
                email : str = None,
                user_type : int = None,
                last_login : int = None,
                created_at : int = None,
                ) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__username = username
        self.__password = password
        self.__email = email
        self.__user_type = user_type
        self.__last_login = last_login
        self.__created_at = created_at

    def getID(self) -> int:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
    
    def getSurname(self) -> str:
        return self.__surname
    
    def getUsername(self) -> str:
        return self.__username

    def getPassword(self) -> str:
        return self.__password

    def getEmail(self) -> str:
        return self.__email

    def getUserType(self) -> int:
        return self.__user_type

    def getLastLogin(self) -> int:
        return self.__last_login

    def getCreatedAt(self) -> int:
        return self.__created_at

    def setID(self,id : int) -> None:
        self.__id = id
        
    def setName(self,name : str) -> None:
        self.__name = name
        
    def setSurname(self,surname : str) -> None:
        self.__surname = surname
        
    def setUsername(self,username : str) -> None:
        self.__username = username

    def setPassword(self,password : str) -> None:
        self.__password = password

    def setEmail(self,email : str) -> None:
        self.__email = email

    def setUserType(self,user_type : int) -> None:
        self.__user_type = user_type

    def setLastLogin(self,last_login : int) -> None:
        self.__last_login = last_login

    def setCreatedAt(self,created_at : int) -> None:
        self.__created_at = created_at
    
    def __iter__(self):
        for key in self.__dict__:
            keyClear = key.replace("_User__","")
            yield keyClear, getattr(self, key)