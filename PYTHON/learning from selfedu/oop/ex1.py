class Point:
    "Класс описание  получить инфу можно черех Point.__doc__"
    color = 'red'
    circle = 2


b = Point()
c = Point()
# python console
# Point.__dict__
# type (b)

setattr(Point, "new_1", 3)  #возможность добавить атрибут
b.x= 1                      #возможность изменить атрибут

getattr(Point, "color ", False) #возможность получить атрибут
print(b.x)                      #возможность получить атрибут

hasattr(b, "color")             #возможность проверить наличие атрибута

delattr(Point, "circle")        #возможность удалить атрибут
del Point.color                 #возможность удалить атрибут

print(b.__dict__)               #возможность получить все атрибуты
print(Point.__doc__)            #возможность получить описание

