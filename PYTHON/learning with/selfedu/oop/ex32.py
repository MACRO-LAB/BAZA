"""#32. Менеджеры контекстов. Оператор with | Объектно-ориентированное программирование Python

Менеджер контекста состоит из __enter__ и __exit__

"""


class DefenedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return  self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [2, 3,4]

try:
    with DefenedVector(v1) as dv:
        for i , a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("error")

print(v1)
