<div style="text-align: center">
    <h1>PYTHON OOP</h1>
</div>

<details>
    <summary>1.1 Класс или объект?</summary>
Класс — это шаблон или чертеж для создания объектов. Он описывает, какие данные (атрибуты) и действия (методы) будут у объектов.
Объект — это экземпляр класса. Это конкретная реализация класса, которая содержит данные и может выполнять действия.

Пример:
```python
# Класс — это "чертеж" для создания объектов
class Dog:
    pass

# Объект — это конкретный экземпляр класса
my_dog = Dog()
```
</details>



<details>
    <summary>1.2 Атрибуты и методы</summary>
Атрибуты — это переменные, которые принадлежат объекту. Они хранят данные объекта.
Методы — это функции, которые принадлежат объекту. Они определяют поведение объекта.

Пример:
```python
class Dog:
    # Атрибут класса (общий для всех объектов)
    species = "Canis familiaris"

    # Метод инициализации (конструктор)
    def __init__(self, name, age):
        # Атрибуты объекта
        self.name = name
        self.age = age

    # Метод объекта
    def bark(self):
        return f"{self.name} говорит: Гав!"
```
</details>


<details>
    <summary>1.3 Инициализатор</summary>
Инициализатор — это специальный метод __init__, который автоматически вызывается при создании объекта. Он используется для установки начальных значений атрибутов объекта.

Пример:
```python
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"{self.name} говорит: Мяу!"

```
</details>


<details>
    <summary>2.1 Наследование</summary>
Наследование — это механизм, который позволяет создавать новый класс на основе существующего. Новый класс (дочерний) наследует атрибуты и методы родительского класса и может добавлять свои собственные.

Пример:
```python
# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук."

# Дочерний класс
class Dog(Animal):  # Наследуемся от Animal
    def bark(self):
        return f"{self.name} говорит: Гав!"

# Создаем объект дочернего класса
my_dog = Dog("Бобик")

# Используем методы родительского и дочернего классов
print(my_dog.speak())  # Метод родительского класса
print(my_dog.bark())   # Метод дочернего класса
```
Добавление атрибутов в класс
Атрибуты — это переменные, которые принадлежат объекту. Они хранят данные объекта. Атрибуты можно добавлять в класс через метод __init__ (инициализатор).

Пример:
```python
class Car:
    def __init__(self, brand, model, year):
        # Добавляем атрибуты
        self.brand = brand
        self.model = model
        self.year = year
```
*    self.brand, self.model, self.year — это атрибуты объекта.
*    brand, model, year — это параметры, которые передаются при создании объекта.

super() — это функция, которая позволяет вызывать методы родительского класса из дочернего класса. Она часто используется в методе __init__, чтобы не дублировать код.

Пример:
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model} age: {self.year}"

class ElectricCar(Car):  # Наследуемся от Car
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Вызов конструктора родительского класса
        self.battery_capacity = battery_capacity  # Новый атрибут

    def charge(self):
        return f"Зарядка {self.brand} {self.model} с батареей {self.battery_capacity} kWh."

# Создаем объект
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
```
*   `super().__init__(brand, model, year) ` вызывает метод `__init__` родительского класса Animal и устанавливает атрибут name.
*   После этого можно добавлять новые атрибуты, например, `battery_capacity`.

Если тебе хочется уменьшить дублирование, можно передавать параметры в виде словаря:
В классах `**kwargs` часто используется для передачи произвольных именованных аргументов в конструктор `__init__`. Это удобно, когда у тебя много атрибутов, и ты не хочешь перечислять их все вручную.
```python
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.age = kwargs.get("age")
        self.city = kwargs.get("city")

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет, я из {self.city}."

person = Person(name="Alice", age=25, city="New York")
print(person.introduce())  # Вывод: Меня зовут Alice, мне 25 лет, я из New York.
```
</details>


<details>
    <summary>2.2 Полиморфизм</summary>
Полиморфизм — это возможность использовать объекты разных классов одинаковым образом. Это означает, что разные классы могут иметь методы с одинаковыми именами, но разной реализацией.
Пример:

```python
class Dog:
    def speak(self):
        return "Гав!"

class Cat:
    def speak(self):
        return "Мяу!"

# Функция, которая работает с любым объектом, у которого есть метод speak
def animal_sound(animal):
    print(animal.speak())

# Создаем объекты
dog = Dog()
cat = Cat()

# Вызываем функцию для разных объектов
animal_sound(dog)  # Вывод: Гав!
animal_sound(cat)  # Вывод: Мяу!
```
</details>


<details>
    <summary>2.3 Инкапсуляция</summary>
Инкапсуляция — это механизм, который позволяет скрыть внутренние детали реализации класса от внешнего мира. Это делается для того, чтобы:

*   Защитить данные от неправильного использования.
*   Упростить взаимодействие с объектом, скрыв сложную логику.
В Python инкапсуляция реализуется с помощью приватных атрибутов и методов.
Приватные атрибуты и методы обозначаются с помощью двойного подчеркивания `__` в начале имени. Они не могут быть доступны напрямую извне класса.
Пример:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance

# Создаем объект
account = BankAccount(1000)

# Пополняем счет
account.deposit(500)

# Снимаем деньги
account.withdraw(200)

# Получаем баланс
print(account.get_balance())  # Вывод: 1300

# Попытка получить доступ к приватному атрибуту
print(account.__balance)  # Ошибка: AttributeError
```
</details>


<details>
    <summary>2.4 Композиция</summary>
Композиция — это способ организации кода, при котором один класс содержит объекты других классов. Это позволяет создавать более сложные структуры, комбинируя простые компоненты.

Пример с множеством объектов, обычный вызов `self.wheels = Wheel()`

```python
class Wheel:
    def rotate(self):
        return "Колесо вращается"

class Car:
    def __init__(self):
        self.wheels = [Wheel() for _ in range(4)]  # 4 колеса

    def drive(self):
        result = ", ".join(wheel.rotate() for wheel in self.wheels)
        return f"Машина едет: {result}"

# Создаем объект
my_car = Car()
print(my_car.drive())
```
</details>


<details>
    <summary>2.5 Перегрузка операторов</summary>
Перегрузка операторов — это возможность изменять поведение стандартных операторов

Например, `+, -, *, /, ==, <` и т.д. для объектов пользовательских классов. 
Это делается с помощью специальных методов, таких как `__add__, __sub__, __eq__` и других.
Пример:
`other` — это просто имя параметра, которое используется в методах перегрузки операторов. Оно обозначает другой объект, с которым выполняется операция. Например, если ты пишешь v1 + v2, то:

`v1`— это объект, для которого вызывается метод `__add__`.

`v2` — это объект, который передается в параметр other.

Как это работает?
Когда ты пишешь v1 + v2, Python автоматически вызывает метод `__add__` у объекта v1 и передает v2 в качестве аргумента other.

Внутри метода `__add__`:
self — это v1.
other — это v2.
Ты можешь использовать self и other, чтобы получить доступ к атрибутам обоих объектов и выполнить нужные операции.
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # self — это текущий объект (например, v1)
        # other — это другой объект (например, v2)
        return Vector(self.x + other.x, self.y + other.y)

# Создаем объекты
v1 = Vector(1, 2)  # self будет v1
v2 = Vector(3, 4)  # other будет v2

# Складываем векторы
v3 = v1 + v2  # Вызывается v1.__add__(v2)
print(v3.x, v3.y)  # Вывод: 4 6
```
Пример с дробями:
```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        # self — текущая дробь (например, f1)
        # other — другая дробь (например, f2)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Создаем объекты
f1 = Fraction(1, 2)  # self будет f1
f2 = Fraction(3, 4)  # other будет f2

# Складываем дроби
f3 = f1 + f2  # Вызывается f1.__add__(f2)
print(f3)  # Вывод: 10/8
```
Разберем шаги:
Когда ты пишешь f1 + f2, Python вызывает метод `__add__` у объекта f1 и передает f2 в качестве аргумента other.

1. Внутри метода `__add__`:
2. self.numerator — это числитель f1 (1).
3. self.denominator — это знаменатель f1 (2).
4. other.numerator — это числитель f2 (3).
5. other.denominator — это знаменатель f2 (4).
6. Выполняется сложение дробей:
7. Новый числитель: 1 * 4 + 3 * 2 = 4 + 6 = 10.
8. Новый знаменатель: 2 * 4 = 8.
9. Возвращается новый объект Fraction(10, 8).
</details>