class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):  # инициализатор класса
        print(f"вызов INIT  {str(self)}")
        self.x = x
        self.y = y

    def __del__(self):  # финализатор класса
        print(f"вызов DEL {str(self)}")

    def set_coords(self, x, y):
        setattr(self, "x", x)
        setattr(self, "y", y)

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.get_coords())
pt.get_coords()

