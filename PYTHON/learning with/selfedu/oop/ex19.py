"""19. Магические методы __iter__ и __next__ | Объектно-ориентированное программирование Python

__iter__ - возвращает итератор

__next__ - возвращает следующее значение"""

class FRange :
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self,):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(1, 10, 2)
# print(next(fr))
# print(next(fr))

for x in fr:
    print(x)


class FRange2D :
    def __init__(self, start=0.0, stop=0.0, step=1.0 , rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

fr = FRange2D(1, 10, 2, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()