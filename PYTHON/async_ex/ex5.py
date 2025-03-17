"""
Библиотеки асинхронные:
    aiohttp
    aiogram
    aiosqlite
    SQLAlchemy
    aiofiles
    io_uring - люнекс https://habr.com/ru/articles/589389/
"""
import asyncio
from time import time



async def do_smht(sec):
    await asyncio.sleep(sec)
    print("fesult ", sec)

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)
    await do_smht(sec)


async def main():
    async  with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))


start = time()
asyncio.run(main())
print(f"Время на работу {time() - start}")
