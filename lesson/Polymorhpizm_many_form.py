# Полиморфизм - это механизм, позволяющий выполнять один и тот же код по-разному (МНОГО ФОРМ)
# Ducktyping (УТИНАЯ ТИПИЗАЦИЯ) - наличие поведения для использования в полиморфизме
# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип), для Питона важно что ты умеешь (поведение)

class SQLiteDatabase:
    def connect(self):
        print('Connecting to database SQLiteDatabase')

    def get_users(self):
        print('get users with SQL')

class MongoDatabase:
    def connect(self):
        print('Connecting to database MongoDatabase')

    def get_users(self):
        print('get users with NoSQL')

# class Postgre:
#     def connect(self):
#         print('Connecting to database Postgre')
#
#     def get_users(self):
#         print('get users with Postgre')


class Server:
    def get_users(self, db):
        # db = Postgre()
        db.connect()
        users = db.get_users()
        return users

# class Server:
#     def get_users(self, db):
#         # db = SQLiteDatabase()
#         db.connect()
#         users = db.get_users()
#         return users

# class Server:
#     def get_users(self):
#         db = SQLiteDatabase()
#         db.connect()
#         users = db.get_users()
#         return users

def get_db_from_config():
    print('read config')
    return MongoDatabase()

def calc(a:int, b:int):
    return a+b

class FakeDb:
    def connect(self):
        pass

    def get_users(self):
        return [1]

if __name__ == '__main__':
    # server = Server()
    # server.get_users(MongoDatabase())
    # server.get_users(Postgre())
    # server.get_users(MongoDatabase())
    # server.get_users(get_db_from_config())
    # print(1) # polymoprh
    # print(10.50) # polymoprh
    # print(None) # polymoprh
    # print('stroka') # polymoprh
    # print(['stroka']) # polymoprh
    # print(calc('1', 'f'))
    server = Server()
    assert [1] == server.get_users(FakeDb())



# Primer 1
# class Animal:
#     def make_noise(self):
#         print('shh')
#
# class Cat(Animal):
#     def make_noise(self):
#         print('meow')
#
# class Dog(Animal):
#     def make_noise(self):
#         print('gavv')
#
#
# class Car:
#     def make_noise(self):
#         print('bi-bi')
#
#     def cool(self):
#         print('new')
#
#
# def noise(animal: Animal):
#     animal.make_noise()
#
# def cool(anim):
#     print('new')
#
#
# if __name__ == '__main__':
#     noise(Cat())
#     noise(Dog())
#     noise(Car())



# primer Java-Polymorphizm
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# def add(a: str, b: str) -> str:
#     return f'{a}{b}'
#
#
# def add(a: float, b: float) -> float:
#     return round(a + b, 3)
#
# if __name__ == '__main__':
#     add(1, 1)