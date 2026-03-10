# 🐍 Python OOP Cheat Sheet

Базовая шпаргалка по Объектно-Ориентированному Программированию в Python. Только самое необходимое для работы.

## 🏗 Классы и Объекты

### Определение класса
```python
class MyClass:
    # Конструктор (вызывается при создании)
    def __init__(self, name, age):
        self.name = name  # Атрибут объекта
        self.age = age
    
    # Метод объекта
    def greet(self):
        return f"Привет, {self.name}"

# Создание объекта (экземпляра)
obj = MyClass("Alex", 25)
print(obj.greet())
```

### `self`
*   Это ссылка на текущий объект.
*   Всегда первый аргумент в методах класса.
*   Нужен для доступа к атрибутам (`self.name`) и другим методам.

## 🧬 Наследование

### Базовый синтаксис
```python
class Parent:
    def speak(self):
        return "Родитель"

class Child(Parent):  # Наследуем от Parent
    def speak(self):  # Переопределение метода
        return "Ребенок"

c = Child()
print(c.speak())  # "Ребенок"
```

### `super()`
Вызов методов родительского класса.
```python
class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # Вызов конструктора родителя
        self.school = school
```

## 🔒 Инкапсуляция (Доступ)

| Префикс | Доступ | Описание |
| :--- | :--- | :--- |
| `name` | Public | Доступен везде. |
| `_name` | Protected | Доступен внутри класса и наследников (соглашение). |
| `__name` | Private | Доступен только внутри класса (имя скрывается). |

```python
class Bank:
    def __init__(self):
        self.public = 100
        self._protected = 200
        self.__private = 300  # Нельзя вызвать напрямую извне
```

## ⚡ Свойства (@property)

Красивая замена геттерам и сеттерам.
```python
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Геттер
        return self._name.upper()

    @name.setter
    def name(self, value):  # Сеттер
        if not value:
            raise ValueError("Имя не пустое!")
        self._name = value

u = User("max")
print(u.name)  # Вызывается как атрибут, работает как метод
u.name = "alex"
```

## 🪄 Магические методы (Dunder)

Методы, которые вызываются автоматически.

| Метод | Когда вызывается | Пример |
| :--- | :--- | :--- |
| `__str__` | `print(obj)` | Возврат строки для пользователя. |
| `__repr__` | `obj` в консоли | Возврат строки для разработчика. |
| `__len__` | `len(obj)` | Длина объекта. |
| `__eq__` | `obj1 == obj2` | Сравнение на равенство. |
| `__add__` | `obj1 + obj2` | Сложение объектов. |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

## 🛠 Статические и Классовые методы

| Декоратор | Описание | Первый аргумент |
| :--- | :--- | :--- |
| (обычный) | Метод объекта | `self` (экземпляр) |
| `@classmethod` | Метод класса | `cls` (класс) |
| `@staticmethod` | Обычная функция в классе | Нет (аргументы как угодно) |

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b  # Не нужен self или cls

    @classmethod
    def create_zero(cls):
        return cls(0)  # Может создать экземпляр класса
```

## 🎁 Dataclasses (Python 3.7+)

Автоматическое создание классов для хранения данных.
```python
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1  # Значение по умолчанию

# __init__, __repr__, __eq__ создаются автоматически
item = Item("Apple", 1.5)
print(item)  # Item(name='Apple', price=1.5, quantity=1)
```

## ⛔ Частые ошибки

1.  **Забыть `self`** в методах: `def method():` ❌ -> `def method(self):` ✅
2.  **Изменение класса вместо объекта**:
    *   ❌ `MyClass.var = 1` (меняет для всех)
    *   ✅ `self.var = 1` (меняет для объекта)
3.  **Вызов метода без скобок**: `obj.method` ❌ -> `obj.method()` ✅
4.  **Использование `__private`**: Лучше использовать `_protected`, так как `__` усложняет наследование.

## 🏁 Шаблон хорошего класса

```python
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected
    
    def __str__(self):
        return f"Worker: {self.name}"
    
    @property
    def salary(self):
        return self._salary
    
    def work(self):
        return f"{self.name} работает"
```