""""18. Магические методы __getitem__, __setitem__ и __delitem__ | ООП Python"""

"""__getitem__(self,item) - получение значения по ключу item"""

"""__setitem__(self,key,value) - установка значения по ключу key на value"""

"""__delitem__(self,key) - удаление значения по ключу key"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0<= item < len(self.marks):
            return self.marks[item]
        else:
            return IndexError("нет такого индекса")

    def __setitem__(self, key, value):
        if  isinstance(key, int) or key <0:
            self.marks[key] = value
        else:
            raise TypeError("Отрицательные индексы запрещены")

    def __delitem__(self, key):
            del self.marks[key]

s1 = Student("Ivan", [5, 4, 4, 5])
print(s1[10])

s1[2] = -9
print(s1[2])

del s1[2]
print(s1.marks)