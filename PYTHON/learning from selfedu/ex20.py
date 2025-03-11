"""20. Наследование в объектно-ориентированном программировании | ООП Python"""


class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 #       self.draw()     # способом вызова родительского метода не стоит пользоваться

    def draw(self):
        return "Рисование геометрического объекта"


class Line(Geom):
    name = "Line"
    def draw(self):
        return "Рисование линии"


class Rect(Geom):
    # def draw(self):
    #     print("Рисование прямоугольника")
    pass


l = Line()
r= Rect()
l.set_coords(1, 2, 3, 4)
r.set_coords(5, 6, 7 ,8)
print(l.__dict__, r.__dict__, sep="\n")

print(l.name, r.name)
print(l.draw(), r.draw())