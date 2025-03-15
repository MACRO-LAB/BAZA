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
    <summary>Библиотеки асинхронные</summary>

*   aiohttp
*   aiogram
*   aiosqlite
*   SQLAlchemy
*   aiofiles
*   [io_uring](https://habr.com/ru/articles/589389/) - люнекс
</details>