"""#28. Введение в обработку исключений. Блоки try / except | ООП Python
* исключения в момент исполнения программы
* исключения при компиляции программы
Учитывать иерархию исключений, так как если поместить к примеру ValueError после Exception, то все исключения будут обрабатываться Exception
"""
try :
    f = open("ex272.py")
except FileNotFoundError:
    print("файл не найден")

print('end')


try:
    x,y = map(int, input().split())
    res = x / y

except ValueError:
    print('неверные данные')
except ArithmeticError:
    print('деление на ноль')
# except (ValueError, ZeroDivisionError):
#     print('неверные данные')

except:
    """Обработка всех исключений"""
    print('что-то пошло не так')