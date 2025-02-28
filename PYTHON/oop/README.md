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
</details>