"""#31. Инструкция raise и пользовательские исключения | ООП Python
BaseException
"""

class ExceptionPrint(Exception):
    """Класс исключения пот отправки данных в принтер"""
    pass

class ExceptionPrintData(ExceptionPrint):
    """Класс исключения пот отправки данных в принтер"""
    def __init__(self,*args):
        self.message = args[0] if args else  None

    def __str__(self):
        return f"Ошибка -> {self.message}"

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать данных {data}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintData("Принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
# p.print("123")
try:

    p.print("123")
except ExceptionPrintData:
    print("except: Принтер не отвечает")
except ExceptionPrint:
    print("except: Принтер не отвечает ExceptionPrint")