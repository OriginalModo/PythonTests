class First:
    def __init__(self):
        self._login = 'login'
        self.__password = 'password'

class Second(First):
    def __init__(self):
        super().__init__()
        self._login = 'new_login'
        self.__password = 'new_password'  # Будет новая переменная

if __name__ == '__main__':
    first = First()
    second = Second()
    print(dir(second))
    print(second._login)
    print(second._Second__password)
    print(second._First__password)



# class Engine:
#     pass
#
#
# class Wheel:
#     pass
#
#
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#         self.wheels = [Wheel()] * 4

    # def start(self):
    #     self.engine.start()


# class Empty(object):
#     pass
#
#
# if __name__ == '__main__':
#     print(dir(Empty))

# class MyList(list):
#     def __str__(self):
#         return super().__str__().replace(',', '\n')
#
# if __name__ == '__main__':
#     print([1, 2, 3])
#     my_list = MyList([1, 2, 3])
#     print(my_list)
#     print(my_list[1])
#     my_list.extend([4, 5])
#     print(list)
#     print(dir(my_list))
