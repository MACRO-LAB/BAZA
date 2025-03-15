"""https://www.youtube.com/watch?v=_4QY1nGFRY8&t=906s&ab_channel=PythonHubStudio"""

"""
1 - Нельзя использовать в асинхронном режиме блокирующие операции на подобии input() - все колом встает
    time.sleep() - для asyncio не подойдет , используем asyncio.sleep()
"""

import time
import os


def clock():
    time_0 = round(time.time())
    while True:
        if (round(time.time()) - time_0) % 5 == 0:
            yield "5 sec"
        else:
            # input()
            yield 0


def query():
    for i in os.walk("D:\\"):
        yield i[0]


def main():
    data = query()
    alarm = clock()
    while True:
        d = next(data)
        a = next(alarm)
        print(d[0])
        if a: print(a)
        time.sleep(1)


main()
