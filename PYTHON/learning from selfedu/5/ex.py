"""5. Методы класса (classmethod) и статические методы (staticmethod) | ООП Python"""

""""Декоратор classmethod"""
""""Декоратор staticmethod"""
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls,arg):
        return  cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        "if Vector.validate(x) and Vector.validate(y):"
        if self.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

        "print(Vector.norm2(self.x, self.y))"
        print(self.norm2(self.x,self.y))


    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x,y):
        "Не рекомендуется, так как если изменится имя Класса , то не будет работать"
        return x*x + y*y + Vector.MAX_COORD

v= Vector(10,20)
print(Vector.validate(10))
res = Vector.get_coord(v)
print(res)

print(Vector.norm2(5,6))
