"""
Пример запроса погоды по городам
"""
from pprint import pprint
import asyncio
import time
from aiohttp import ClientSession

from datetime import datetime

# Получаем текущее время
now = datetime.now()


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56' , "units": 'metric'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            pprint(f'{city}: temp :{weather_json["main"]["temp"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Irkutsk', "Svirsk", 'Krasnodar']

print(time.time())
a = (time.time())
asyncio.run(main(cities))

print(time.time())
print(f"Время на работу {time.time() - a}") #print(time.time()-a)

