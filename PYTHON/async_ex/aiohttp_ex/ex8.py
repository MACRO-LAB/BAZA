import asyncio
import json
from aiohttp import ClientSession, web


# Асинхронная функция для получения погоды по названию города
async def get_weather(city):
    # Создаем новую HTTP-сессию для запросов к API
    async with ClientSession() as session:
        # URL API OpenWeatherMap для получения текущей погоды
        url = f'http://api.openweathermap.org/data/2.5/weather'

        # Параметры запроса: название города и ключ API
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        # Делаем GET-запрос к API
        async with session.get(url=url, params=params) as response:
            # Получаем JSON ответ от API
            weather_json = await response.json()

            # Пробуем получить основную информацию о погоде
            try:
                return weather_json["weather"][0]["main"]
            except KeyError:
                # Если данные отсутствуют или структура ответа неверная
                return 'Нет данных'


# Функция обработчик HTTP-запросов
async def handle(request):
    # Извлекаем параметр 'city' из URL запроса
    city = request.rel_url.query['city']

    # Получаем информацию о погоде асинхронно
    weather = await get_weather(city)

    # Формируем словарь с результатами
    result = {'city': city, 'weather': weather}

    # Возвращаем JSON-ответ клиенту
    return web.Response(text=json.dumps(result, ensure_ascii=False))


# Основная функция запуска сервера
async def main():
    # Создаем приложение aiohttp
    app = web.Application()

    # Регистрируем маршрут для обработки GET-запросов к /weather
    app.add_routes([web.get('/weather', handle)])

    # Создаем и запускаем веб-сервер
    runner = web.AppRunner(app)
    await runner.setup()

    # Запускаем сервер на localhost:8080
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    # Цикл для поддержания работы сервера
    while True:
        await asyncio.sleep(3600)


# Запуск сервера если скрипт выполняется напрямую
if __name__ == '__main__':
    asyncio.run(main())