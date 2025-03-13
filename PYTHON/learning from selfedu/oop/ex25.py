"""#25. Множественное наследование | Объектно-ориентированное программирование Python
MRO - Method Resolution Order , при использовании множественного наследования  super().__init__() позволяет вызвать конструктор других родительский классов
__mro__ - список классов в порядке наследования
"""

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"name: {self.name}, weight: {self.weight}, price: {self.price}")

class MixinLog:
    ID= 0

    def __init__(self,):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def safe_sell_log(self):
        print(f" {self.id} safe_sell_log")

    def print_info(self):
        print(f"print_info из MixinLog")

class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)

n = NoteBook("NoteBook", 1, 1000)
n.print_info()
n.safe_sell_log()
print(NoteBook.__mro__)