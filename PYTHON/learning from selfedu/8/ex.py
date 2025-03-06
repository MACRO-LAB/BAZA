"""Паттерн "Моносостояние" | Объектно-ориентированное программирование Python"""


class ThreadData:
    """получилось что эти атирубыты если меня в каком нибудь экземпляре, то меняенься во всех экземплярах
    так же можно создавать и новые , которые так же будет для всех едины
    """
    __shared_arrrs__ = {
        'name' : 'thread_1',
        'data' : {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_arrrs__


th_1 = ThreadData()
th_2 = ThreadData()
th_2.id = 3
th_1.attr_new = "new"