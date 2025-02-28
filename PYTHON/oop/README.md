<div style="text-align: center">
    <h1>PYTHON OOP</h1>
</div>

<details>
    <summary>1.1 Класс или объект?</summary>
Что такое класс?
Класс — это шаблон или чертеж для создания объектов. Он описывает, какие данные (атрибуты) и действия (методы) будут у объектов.

Что такое объект?
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
Атрибуты
Атрибуты — это переменные, которые принадлежат объекту. Они хранят данные объекта.

Методы
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

# Создаем объект
my_dog = Dog("Бобик", 3)

# Доступ к атрибутам
print(my_dog.name)  # Вывод: Бобик
print(my_dog.age)   # Вывод: 3

# Вызов метода
print(my_dog.bark())  # Вывод: Бобик говорит: Гав!
```
</details>


<details>
    <summary>1.3 Инициализатор</summary>
Что такое инициализатор?
Инициализатор — это специальный метод __init__, который автоматически вызывается при создании объекта. Он используется для установки начальных значений атрибутов объекта.

Пример:
```python
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"{self.name} говорит: Мяу!"

# Создаем объект
my_cat = Cat("Мурзик", "рыжий")

# Доступ к атрибутам
print(my_cat.name)   # Вывод: Мурзик
print(my_cat.color)  # Вывод: рыжий

# Вызов метода
print(my_cat.meow())  # Вывод: Мурзик говорит: Мяу!
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
</details>