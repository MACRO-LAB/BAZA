"""16. Магические методы __eq__ и __hash__ | Объектно-ориентированное программирование Python"""

"""__eq__ - равенство"""

"""__hash__ - хэш-функция"""

"""Если объекты a==b то a.__hash__() == b.__hash__()"""
"""Если хэши равны, не гарантирует равенство объектов"""
"""Если хэши не равны,объекты точно не равны"""
"""только для неизменяйщих объектов, то-есть для hash([1,2,3]) будет ошибка"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1=Point(1,2)
p2=Point(1,2)
print(hash(p1), end="\n")
print(hash(p2), end="\n")
print(p1 == p2)