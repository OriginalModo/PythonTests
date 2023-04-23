# Паттерн или шаблон разработки - это общие способы решения частых задач и проблем
# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию, обьект всегда 1
# Monostate Одиночка - это шаблон предоставления глобального доступа к состоянию, обьекты могут быть разными
# нужен для одной точки доступа к реусурсам/данным и для того чтобы ресурсоемкие задачи сделать 1 раз
# плюсы: 1 раз выполняем тяжелые задачи, имеет 1 вход для всей системы
# минусы : общесистемная глобальная переменная
# модуль в python - это синглтон

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        # parse, db, work with data/resourses etc...
        self.data = 101

class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # parse, db, work with data/resourses etc...
            self.data = 101


if __name__ == '__main__':
    first = Monostate()
    print(first)
    second = Monostate()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)
    print(Monostate())


