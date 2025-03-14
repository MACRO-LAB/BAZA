"""
#37. Введение в Python Data Classes (часть 1) | Объектно-ориентированное программирование Python
__repr__
@dataclass
если сравнивать обьекты на равенство (td == td2). __eq__  будет сравнивать не по номеру обьекта, а по содержимому
Нельзя устаовить атрибуты изменяемые по типу списка [], так как это список для всех обьектов
нужно пользовать спец функцинй field()
"""
from  pprint import pprint
from dataclasses import dataclass ,field


class Thing:
    def __init__(self, name, weight, price, dims:[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims


    def __repr__(self):
        return f"Thing : {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: int
    price: int = 0
    """конструкция делает список при каждом запуске пустым, так как list это и есть пустой список"""
    dims: list = field(default_factory=сссс)

    """ __init__ / __repr__ / __eq__  можно переопределить в dataclass """
    def __eq__(self, other):
        return self.price == other.price


t = Thing("телефон", 100, 10000, [10, 20, 30])
print(t)

td = ThingData("телефон", 100, 10000,)


td.dims.append(40)
print(td)
td2 = ThingData("телефон", 100, 10000,)
print(td2)
# pprint(ThingData.__dict__)

# print(td == td2)
