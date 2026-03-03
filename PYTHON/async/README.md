# 🐍 Python Asyncio Cheat Sheet

Краткое руководство по асинхронному программированию в Python.

## ⚡ Основы

| Конструкция | Описание |
| :--- | :--- |
| `async def` | Объявление корутины (асинхронной функции). |
| `await` | Ожидание результата (не блокирует поток). |
| `asyncio.run()` | Запуск цикла событий (точка входа). |
| `asyncio.sleep()` | Асинхронная пауза. **Не использовать `time.sleep`!** |

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(main())
```

## 🚀 Запуск задач

### Параллельно (ждать все)
```python
results = await asyncio.gather(task1(), task2(), task3())
```

### В фоне (не ждать сразу)
```python
task = asyncio.create_task(long_func())
# ... делаем другие дела ...
await task  # Ждем результат позже
```

### По мере готовности
```python
for coro in asyncio.as_completed([task1, task2]):
    res = await coro
```

## 🔒 Синхронизация

### Lock (Блокировка)
```python
lock = asyncio.Lock()
async with lock:
    # Критическая секция
```

### Semaphore (Лимит одновременных)
```python
sem = asyncio.Semaphore(5)  # Макс 5 задач
async with sem:
    await do_work()
```

### Queue (Очередь)
```python
q = asyncio.Queue()
await q.put(item)   # Producer
item = await q.get() # Consumer
q.task_done()
```

## ⏱ Таймауты и Отмена

### Таймаут
```python
try:
    await asyncio.wait_for(func(), timeout=5.0)
except asyncio.TimeoutError:
    pass
```

### Отмена задачи
```python
task.cancel()
# Внутри корутины ловить asyncio.CancelledError
```

## ⛔ Анти-паттерны

| ❌ Нельзя | ✅ Нужно |
| :--- | :--- |
| `time.sleep()` | `await asyncio.sleep()` |
| `requests.get()` | `aiohttp` / `httpx` (async) |
| Тяжелые вычисления (CPU) | `loop.run_in_executor` |
| Забыть `await` | `await func()` или `create_task()` |
| `asyncio.run()` внутри async | Использовать `await` |

## 🛠 Полезные утилиты

- `asyncio.current_task()` — текущая задача.
- `asyncio.shield(task)` — защита от отмены.
- `asyncio.to_thread(func)` — запуск sync функции в потоке (3.9+).