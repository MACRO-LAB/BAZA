"""15. Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие | ООП Python

__eq__ - равенство
__ne__ - не равенство
__lt__ - меньше
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно"""

class Clock:
    __DAY = 86400  # секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError ("секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verifi_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен быть целым числом или объектом Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verifi_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verifi_data(other)
        return self.seconds < sc


c1= Clock(1000)
c2= Clock(2000)

# print(c1, c2)
print(c1 == c2)
print(c1 != c2) # not (c1 == c2)  если не реализовано __ne__ автоматически делается так
print(c1 < c2)
print(c1 > c2) # not (c1 < c2)   если не реализовано __gt__ автоматически делается так