"""
#39. Python Data Classes при наследовании | Объектно-ориентированное программирование Python


"""

from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def defget_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    cyrrent_uid = 0
    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post init")
        Goods.cyrrent_uid += 1
        self.uid = Goods.cyrrent_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = None
    measure: list = field(default_factory=GoodsMethodsFactory.defget_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print("Book: post init")


print(GoodsMethodsFactory.defget_init_measure())
b = Book(1000, 100, "Python ", "Балакиев")
print(b)


class Car:
    def __init__(self, model, max_speed, price):
        self.medel = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass("CarData",
                         [
                             "model",
                             "max_speed",
                             ("price", float, field(default=0))],
                         namespace={"get_max_speed": lambda self: self.max_speed})

c = CarData("BMW", 300)
print(c)
print(c.get_max_speed())
