"""Магический метод __bool__ определения правдивости объектов | ООП Python"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len")
        return self.x * self.y

    def __bool__(self):
        """приоритет вызова __bool__ больше, чем __len__"""
        print("__bool")
        return self.x == self.y

p = Point(10, 2)

print(bool(p))