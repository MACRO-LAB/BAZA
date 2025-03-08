"""Магические методы __str__, __repr__, __len__, __abs__ | ООП Python"""

class Cat :
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return "выводится при мспользовании print"

    def __repr__(self):
        """для разрабов в откладке программы (python console)"""
        return f"{self.__class__} : {self.name} "
        #Выведет :  <class '__main__.Cat'> : Мурзик

    def __len__(self):
        """ожно их переопределить всячески, просто в return казать что выводить"""
        return 5

    def __abs__(self):
        return 7

cat = Cat("Мурзик")

print(cat)
print(len(cat))
print(abs(cat))



