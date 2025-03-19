import asyncio
from proxybroker import Broker
import  os

# Устанавливаем SelectorEventLoop для Windows
if os.name == 'nt':  # Проверяем, что система — Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)

async def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)

    # Запуск задач
    tasks = asyncio.gather(
        broker.find(types=['HTTP', 'HTTPS'], limit=10),
        show(proxies)
    )

    await tasks

# Запуск асинхронного кода
if __name__ == '__main__':
    asyncio.run(main())