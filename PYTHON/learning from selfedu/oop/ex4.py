"""4. Магический метод __new__. Пример паттерна Singleton | Объектно-ориентированное программирование"""


#__new___ - метод, вызываемый при создании экземпляра класса
class DataBase:

    def __new__(cls, *args, **kwargs):
        print(f"вызов __new__ для {str(cls)}")
        return super().__new__(cls)

    def __init__(self, x=0,y=0):
        print(f"вызов INIT  {str(self)}")
        self.x = x
        self.y = y

# p=Point(y=1,x=2)
# print(p )

    """1. Пример паттерна Singleton Синглтон (Singleton) в Python — это шаблон проектирования, 
    который гарантирует, что у класса будет только один экземпляр, 
    и предоставляет глобальную точку доступа к этому экземпляру. 
    """

class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
        print(f"вызов DEL {str(self)}")

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f"Подключение к базе данных {self.user}:{self.password}@{self.port}")

    def close(self):
        print(f"Отключение от базы данных")

    def read(self):
        print(f"Чтение данных из базы данных ")

    def write(self,data):
        print(f"Запись данных в базу данных {data}")

db = Database("user", "password", 5432)
db2 = Database("user2", "password2", 543222)
print(id(db), id(db2))
print(db.connect())
print(db2.connect())
