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
# print(c()) 
# print(c())


class TestCallDecorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self,ex_1, *args, **kwargs):
        return f"вызов __call__ c параметром ex_1:({ex_1}) функуией :{self.__func(ex_1)}"

@TestCallDecorator
def test_call(test):
    return f"\ttest_call c аргументом test: {test}"

print(test_call("ЖОПА"))