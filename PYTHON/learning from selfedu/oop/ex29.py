"""#29. Обработка исключений. Блоки finally и else | Объектно-ориентированное программирование Python

"""



try:
    # x,y = map(int, input().split())
    # res = x / y

    with open("ex272.py") as f:
        f.write("hello")
except FileNotFoundError as z:
    print(f'деление на ноль : {z}')
except :
    print(f'Другая ошибка ')
else:
    """Если нет ошибок"""
    print("нет исключений")
finally:
    """Всегда отрабатывает"""
    print(f"принт res : ")

    # if f :
    #     f.close()
    #     print("Файл закрыт")

def get_value():
    try:
        x, y = map(int, input().split())
        """return отрабатывает в последнию очередь"""
        return x , y
    except ValueError as v:
        print(v)
        return 0,0,
    finally:
        print("finally")

x, y = get_value()
print(x,y)