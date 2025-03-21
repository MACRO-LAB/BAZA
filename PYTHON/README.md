<div style="text-align: center">
    <h1>PYTHON</h1>
</div>

<details>
    <summary>OOP</summary>

*   [OOP](oop/README.md)

</details>


<details>
    <summary>proxy ngrok</summary>
Этот метод использует SOCKS5 протокол с аутентификацией для безопасного подключения к ngrok через ваш прокси-сервер. Все данные передаются зашифрованным способом через прокси.

```python
import socks
import socket

def connect_ngrok_with_proxy():
    # Данные прокси
    proxy_host = '185.***.***.214'
    proxy_port = ***75  # Используем SOCKS5 порт
    proxy_user = '***'
    proxy_pass = '***'
    
    # Данные ngrok
    ngrok_host = '0.tcp.ngrok.io'  # Адрес ngrok
    ngrok_port = ***06  # Порт ngrok
    
    # Настройка прокси
    socks.set_default_proxy(
        socks.SOCKS5,
        proxy_host,
        proxy_port,
        True,  # Режим аутентификации
        username=proxy_user,
        password=proxy_pass
    )
    
    # Замена стандартного сокета
    socket.socket = socks.socksocket
    
    # Создание соединения
    return socket.create_connection((ngrok_host, ngrok_port))
```
Использование с HTTP-запросами
```python
import socks
import socket
import urllib.request

def connect_with_socks():
    # Данные прокси
    proxy_host = '185.***.***.214'
    proxy_port = ***74  # Используем HTTP порт
    proxy_user = '***'
    proxy_pass = '***'
    
    # Настройка прокси
    socks.set_default_proxy(
        socks.SOCKS5,
        proxy_host,
        proxy_port,
        True,
        username=proxy_user,
        password=proxy_pass
    )
    
    # Замена стандартного сокета
    socket.socket = socks.socksocket
    
    # Создание opener с прокси
    handler = urllib.request.ProxyHandler({
        'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
        'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}'
    })
    
    return urllib.request.build_opener(handler)
```
Важные замечания по безопасности
Проверьте работоспособность прокси перед использованием:
```python
import socks
try:
    socks.create_connection(('google.com', 80), proxy=('185.***.***.214', 6***5),
                          username='***', password='***')
    print("Прокси работает!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
```
При использовании кода убедитесь что:
*   Установлена библиотека PySocks (pip install pysocks)
*   Адрес и порт ngrok актуальны
*   Логин и пароль от прокси введены правильно
</details>


<details>
    <summary>Чтение больших файлов по строкам используя `yield`</summary>
Генераторы позволяют вам читать файл построчно, что экономит память и делает процесс более эффективным.

```python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('large_file.txt'):
    print(line)
```

</details>

<details>
    <summary>ASUNC</summary>

*   [ASUNC](async_ex/README.md)

</details>

<details>
    <summary>форматировании строк (f-strings, метод format() и другие)</summary>

* В Python синтаксис : используется в форматировании строк (f-strings, метод format() и другие) для указания формата
  вывода значения. После : можно указать различные параметры форматирования, такие как количество знаков после запятой,
  выравнивание, заполнение и т.д.
#### Вот несколько примеров использования : в форматировании строк:
  1. Форматирование чисел с плавающей точкой
     * :.2f — округление до двух знаков после запятой.
      ```python
      value = 3.14159
      print(f"Value: {value:.2f}")  # Вывод: Value: 3.14
      ```
      * :.0f — округление до целого числа.
      ```python
      value = 3.14159
      print(f"Value: {value:.0f}")  # Вывод: Value: 3
      ```
  2. Форматирование целых чисел
     * :d — вывод целого числа.
      ```python
      value = 42
      print(f"Value: {value:d}")  # Вывод: Value: 42
      ```
     * :05d — добавление ведущих нулей до 5 символов.
      ```python
        value = 42
        print(f"Value: {value:05d}")  # Вывод: Value: 00042
      ```
  3. Форматирование строк
       * :<10 — выравнивание строки по левому краю с общей длиной 10 символов.
        ```python
        text = "Hello"
        print(f"Text: '{text:<10}'")  # Вывод: Text: 'Hello     '
        ```
       * :>10 — выравнивание строки по правому краю с общей длиной 10 символов.
        ```python
        text = "Hello"
        print(f"Text: '{text:>10}'")  # Вывод: Text: '     Hello'
        ```
       * :^10 — выравнивание строки по центру с общей длиной 10 символов.
        ```python
        text = "Hello"
        print(f"Text: '{text:^10}'")  # Вывод: Text: '  Hello   '
        ```
  4. Форматирование с заполнением
       * :*^10 — выравнивание по центру с заполнением символа *.
        ```python
        text = "Hello"
        print(f"Text: '{text:*^10}'")  # Вывод: Text: '**Hello***'
        ```
       * :=+10 — выравнивание числа с заполнением нулями после знака.
        ```python
        value = -42
        print(f"Value: {value:=+10}")  # Вывод: Value: -      42
        ```
  5.  Форматирование процентов
       * :.2% — форматирование числа в проценты с двумя знаками после запятой.
        ```python
        value = 0.12345
        print(f"Value: {value:.2%}")  # Вывод: Value: 12.35%
        ```
  6.  Форматирование в научной нотации
       * :.2e — форматирование числа в научной нотации с двумя знаками после запятой.
        ```python
        value = 12345.6789
        print(f"Value: {value:.2e}")  # Вывод: Value: 1.23e+04
        ```
  7.  Форматирование с разделителем тысяч
       * :, — добавление разделителя тысяч.
        ```python
        value = 1000000
        print(f"Value: {value:,}")  # Вывод: Value: 1,000,000
        ```
  8.  Комбинирование форматов
       * Можно комбинировать несколько параметров форматирования.
        ```python
        value = 12345.6789
        print(f"Value: {value:,.2f}")  # Вывод: Value: 12,345.68
        ```

</details>
