"""
#38. Введение в Python Data Classes (часть 2) | Объектно-ориентированное программирование Python
__post_init__  в связке с field(init=False) - нужен для инициализации атрибутов в @dataclass
Функця field():
    repl - буливо значение , указывающее использовать ли атрибут в магическом методе __repr__(). по умолчанию True
    compare - буливо значение , указывающее использовать ли атрибут в магическом методе __eq__(). по умолчанию True
    default: значение по умолчанию



"""

from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_length: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_length else 0
"""Если включены параметрый датакласс, то переопределить маг методы нельзя"""
@dataclass(init=True, repr=True, eq=True, order=True, frozen=False)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int =field(compare=False)
    length: float = field(init=False, compare=False, default=0)
    calc_length: InitVar[bool] = True

    def __post_init__(self,calc_length: bool):
        if calc_length:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1, 2, 3, False)
print(v)