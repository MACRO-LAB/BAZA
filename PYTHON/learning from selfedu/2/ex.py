class Point :
    color = 'red'
    circle = 2

# def det_coords():
#     print("Вызов метода det_coords")

# def set_coords (self):
#     print(f"Вызов метода set_coords {str(self)}")

    def set_coords (self, x ,y):
        self.x = x
        self.y = y

pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)

pt_2 = Point()
pt_2.set_coords(10, 20)
print(pt_2.__dict__)