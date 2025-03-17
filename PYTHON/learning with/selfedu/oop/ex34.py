"""
#34. Метаклассы. Объект type | Объектно-ориентированное программирование Python
#35. Пользовательские метаклассы. Параметр metaclass | ООП Python
#36. Метаклассы в API ORM Django | Объектно-ориентированное программирование Python


"""

class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

A = type('Point', (), {"MAX_COORD": 100, "MIN_COORD": 0})
