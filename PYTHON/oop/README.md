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
`*args` - передача НЕ именованных аргементов
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


<details>
    <summary>2.6 Итераторы</summary>
Итератор — это объект, который позволяет перебирать элементы коллекции (например, списка, словаря или пользовательского объекта) по одному. 

В Python итераторы реализуются с помощью методов `__iter__` и `__next__`.
```python
my_list = [1, 2, 3]
my_iter = iter(my_list)  # Получаем итератор

print(next(my_iter))  # Вывод: 1
print(next(my_iter))  # Вывод: 2
print(next(my_iter))  # Вывод: 3
```
Чтобы создать собственный итератор, нужно:
1.  Реализовать метод `__iter__`, который возвращает сам объект.
2. Реализовать метод `__next__`, который возвращает следующий элемент или вызывает исключение `StopIteration`, если элементы закончились.

Пример итератора для класса:
```python
class Range:
    def __init__(self, start, end, step=1):
        if self.step < 0:
            raise ValueError("Шаг должен быть положительным числом")
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.end
        return self

    def __next__(self):
        if self.current >= self.start:
            result = self.current  # Сохраняем текущее значение
            self.current -= self.step  # Увеличиваем текущее значение на шаг
            return result  # Возвращаем сохраненное значение
        else:
            raise StopIteration

my_range = Range(1, 10, 2)

# Используем итератор
for num in my_range:
    print(num)
```
</details>


<details>
    <summary>2.7 Генераторы</summary>

Генератор — это специальная функция, которая возвращает итератор.

В отличие от обычных функций, генератор использует ключевое слово `yield` для возврата значений по одному. 
Это позволяет генерировать последовательности "на лету", не храня их в памяти целиком.

Генератор vs Итератор:
*   Итератор: Требует создания класса с методами `__iter__` и `__next__`.
*   Генератор: Проще в использовании, так как это обычная функция с `yield`.
Пример генератора для диапазона чисел:
```python
def range_generator(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

# Используем генератор
for num in range_generator(1, 10, 2):
    print(num)
```
## Преимущества и недостатки использования yield
### Преимущества
1. Экономия памяти: Генераторы не загружают всю последовательность данных в память сразу. Это особенно полезно при работе с большими наборами данных или потоками данных.
2. Ленивые вычисления: Данные генерируются по мере необходимости, что позволяет обрабатывать большие объемы данных. Это делает генераторы идеальными для работы с потоками данных в реальном времени.
3. Читаемость кода: Использование yield делает код более понятным и лаконичным. Генераторы позволяют вам создавать функции, которые могут возвращать несколько значений по мере необходимости, что делает код более модульным и легко читаемым.
### Недостатки
1. Одноразовость: Генераторы можно итерировать только один раз. После завершения итерации они не могут быть перезапущены. Это может быть неудобно, если вам нужно повторно использовать генератор.
2. Отладка: Отладка генераторов может быть сложнее из-за их ленивой природы. Поскольку значения генерируются только по мере необходимости, отладка может быть более сложной задачей.
3. Сложность: Для новичков концепция генераторов может быть сложной для понимания. Понимание того, как работают генераторы и как использовать yield, может потребовать
</details>


<details>
    <summary>3.1 self и cls</summary>

`self` — это ссылка на текущий экземпляр класса. 
Он используется для доступа к атрибутам и методам объекта внутри класса.
#### Пример:
```python
class Person:
    def __init__(self, name):
        self.name = name  # self.name — это атрибут объекта

    def greet(self):
        return f"Привет, меня зовут {self.name}!"
```

`cls` — это ссылка на класс. 
Он используется в методах класса (classmethod) для доступа к атрибутам и методам класса, а не объекта.
#### Пример:
```python
class Person:
    count = 0  # Атрибут класса

    def __init__(self, name):
        self.name = name
        Person.count += 1  # получился счетсик объектов

    @classmethod
    def get_count(cls):
        return cls.count  # cls.count — это атрибут класса

# Создаем объекты
person1 = Person("Alice")
person2 = Person("Bob")

# Используем метод класса
print(Person.get_count())  # Вывод: 2
```
</details>


<details>
    <summary>3.2 @staticmethod</summary>
Статический метод — это метод, который принадлежит классу, но не зависит ни от атрибутов класса, 
ни от атрибутов объекта. Он похож на обычную функцию, 
но находится внутри класса для удобства организации кода.

### Пример статического метода:
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Используем статический метод
result = MathUtils.add(5, 3)
print(result)  # Вывод: 8
```
### Зачем нужны статические методы?
* Логическая группировка: Если функция связана с классом, но не использует его атрибуты, её можно сделать статическим методом.
* Удобство: Статические методы можно вызывать без создания объекта класса
</details>



<details>
    <summary>3.3 Сущности и отношения</summary>
В объектно-ориентированном программировании (ООП):

* Сущность — это объект, который представляет что-то значимое в программе (например, человек, машина, заказ).
* Отношение — это связь между сущностями (например, человек владеет машиной, заказ принадлежит клиенту).
```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order :
    def __init__(self,order_id, product, customer):
        self.order_id = order_id
        self.product = product
        self.customer = customer

customer_1 = Customer("John Doe", "oBx2z@example.com")
order_1 = Order(1, "Laptop", customer_1)
result = f"Order ID: {order_1.order_id}, Product: {order_1.product}, Customer: {order_1.customer.name}"
print(result)
```
</details>


<details>
    <summary>3.4 Свойства (Properties)</summary>
Свойства — это способ контролировать доступ к атрибутам объекта. Они позволяют:

* Читать значение атрибута.
* Устанавливать значение атрибута.
* Удалять атрибут.
Свойства создаются с помощью декораторов `@property`, `@<attribute>.setter` и `@<attribute>.deleter`.
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Защищенный атрибут

    @property
    def celsius(self):
        return self._celsius  # Возвращаем значение

    @celsius.setter
    def celsius(self, new_set):
        if new_set > -273.15:
            self._celsius = new_set  # Устанавливаем новое значение
        else:
            raise ValueError("Температура не может быть меньше -273.15")

    @celsius.deleter
    def celsius(self):
        del self._celsius  # Удаляем атрибут

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32  # Возвращаем температуру в Фаренгейтах

# Создаем объект
temp = Temperature(25)

# Используем свойства
print(temp.fahrenheit)  # Вывод: 77.0

# Устанавливаем новое значение
temp.celsius = 30
print(temp.fahrenheit)  # Вывод: 86.0

del temp.celsius  # Удаляем атрибут


```
</details>


<details>
    <summary>Когда использовать _celsius, а когда __celsius?</summary>
`celsius` - название просто для примера

1. `_celsius`:

    * Используй, если хочешь показать, что атрибут не предназначен для публичного доступа, но при этом не хочешь усложнять его использование внутри класса или в подклассах.
    * Это более "мягкий" способ инкапсуляции.

2. `__celsius`:

   * Используй, если хочешь сделать атрибут действительно "приватным" и предотвратить его случайное использование извне.
   * Это более "строгий" способ инкапсуляции.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Защищенный атрибут
        self.__celsius = celsius  # Приватный атрибут

temp = Temperature(25)

# Доступ к защищенному атрибуту
print(temp._celsius)  # Вывод: 25 (но так делать не рекомендуется)

# Доступ к приватному атрибуту
print(temp.__celsius)  # Ошибка: AttributeError
print(temp._Temperature__celsius)  # Вывод: 25 (но так делать не следует)
```
</details>


<details>
    <summary>4. SOLID → 4.1 Принципы</summary>
SOLID — это набор из пяти принципов объектно-ориентированного программирования, которые помогают писать более понятный, 
гибкий и поддерживаемый код. Эти принципы были предложены Робертом Мартином (дядя Боб).

1. S — Single Responsibility Principle (Принцип единственной ответственности):
   * Класс должен иметь только одну причину для изменения (т.е. выполнять только одну задачу).
```python
class Task:
    def __init__(self, description):
        self.description = description

    def display(self):
        return f"Задача: {self.description}"

class TaskSaver:
    @staticmethod
    def save_to_file(task, filename):
        with open(filename, 'w') as file:
            file.write(task)

class TaskNotifier:
    @staticmethod
    def notify(task):
        print(f"Уведомление: {task}")

# Создаем объекты
task = Task("Закончить проект")
task_content = task.display()

# Сохраняем задачу в файл
TaskSaver.save_to_file(task_content, "task.txt")

# Отправляем уведомление
TaskNotifier.notify(task_content)
```
2. O — Open/Closed Principle (Принцип открытости/закрытости):
   * Классы должны быть открыты для расширения, но закрыты для модификации.
```python
#пример где видно в дочерних классах выполняется так же функция generate , тоесть прои расширении не надо дублировать  
class Report:
    def generate(self):
        if not self.content():
            raise ValueError("Отчет не может быть пустым")
        return self.content()

    def content(self):
        raise NotImplementedError("Метод content должен быть переопределен в подклассе")

class HTMLReport(Report):
    def content(self):
        return "<html><body>Отчет в HTML</body></html>"

class PDFReport(Report):
    def content(self):
        return "Отчет в PDF"
#Зачем использовать базовый класс?
# 1. Единый интерфейс:
# Базовый класс определяет общий интерфейс (например, метод generate), который должны реализовать все подклассы. Это позволяет: 
# Упростить использование классов. Например, ты можешь передавать объекты разных подклассов в одну функцию, не заботясь о их конкретном типе.
# Убедиться, что все подклассы реализуют необходимые методы.

# 2. Расширяемость:
# Если ты решишь добавить новый тип отчета (например, CSVReport), тебе не нужно изменять существующий код. Достаточно создать новый подкласс.

# 3. Контроль за реализацией:
# Базовый класс может содержать общую логику или проверки, которые будут унаследованы всеми подклассами. 
# Например, можно добавить проверку на пустой отчет:
```
3. L — Liskov Substitution Principle (Принцип подстановки Барбары Лисков):
   * Объекты в программе должны быть заменяемы экземплярами их подтипов без изменения правильности программы.
4. I — Interface Segregation Principle (Принцип разделения интерфейса):
   * Клиенты не должны зависеть от интерфейсов, которые они не используют.
5. D — Dependency Inversion Principle (Принцип инверсии зависимостей):
   * Модули верхнего уровня не должны зависеть от модулей нижнего уровня. Оба должны зависеть от абстракций.
</details>