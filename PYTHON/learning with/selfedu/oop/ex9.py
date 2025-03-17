""". Свойства property. Декоратор @property | Объектно-ориентированное программирование Python
property - это один из способов определения свойств, что бы не дублировать все свойства в get/set
"""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    "вариант 3"
    @property
    def old(self):
        return self.__old

    "нужно использовать метод из property + добавить .setter"
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    "вариант 1"
    "old = property(get_old, set_old)" #эквивален @property

    "вариант 2"
    "old = property()"
    "old = old.setter(set_old)"
    "old = old.getter(get_old)"

    """с помощью декоратора property можно создать свойство, которое будет обрабатывать get/set
        print(p.old)
        p.old = 30
        print(p.old, p.__dict__)
    """


p = Person("Vasya", 20)
p.__dict__["old"] = "old in obg"
a= p.old
p.old = 35
del p.old
print(p.__dict__)
