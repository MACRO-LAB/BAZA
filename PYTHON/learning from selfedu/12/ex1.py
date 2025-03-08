"""Магический метод __call__. Функторы и классы-декораторы | ООП Python"""
"""dunder - методы которые начинаются и заканчиваются двумя подчеркиваниями"""

class Counter:
    """счетчик вызовов"""
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter


""" скобки после вызова класса это посути вызов __call__ """
c = Counter()
print(c())
print(c())