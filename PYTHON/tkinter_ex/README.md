# 🐍 Python Tkinter Cheat Sheet

Краткое руководство по созданию GUI приложений в Python.

## ⚡ Основы

| Конструкция | Описание |
| :--- | :--- |
| `import tkinter as tk` | Импорт библиотеки. |
| `tk.Tk()` | Создание главного окна. |
| `window.mainloop()` | Запуск цикла событий (обязательно в конце). |
| `window.title("Name")` | Установка заголовка окна. |
| `window.geometry("WxH")` | Установка размера окна. |

```python
import tkinter as tk

root = tk.Tk()
root.title("App")
root.geometry("400x300")
root.mainloop()
```

## 🧩 Виджеты (Widgets)

| Виджет | Описание |
| :--- | :--- |
| `Label` | Текст или изображение. |
| `Button` | Кнопка. |
| `Entry` | Однострочное поле ввода. |
| `Text` | Многострочное поле ввода. |
| `Frame` | Контейнер для группировки. |
| `Checkbutton` | Чекбокс. |
| `Radiobutton` | Радио-кнопка (выбор одного). |
| `Listbox` | Список элементов. |
| `ttk.Combobox` | Выпадающий список (требуется `from tkinter import ttk`). |

```python
lbl = tk.Label(root, text="Hello")
btn = tk.Button(root, text="Click", command=func)
inp = tk.Entry(root)
lbl.pack()
```

## 📐 Layout (Разметка)

### Pack (Упаковка)
Простое размещение сверху вниз / слева направо.
```python
widget.pack(side=tk.LEFT, padx=10, pady=10)
# side: TOP, BOTTOM, LEFT, RIGHT
```

### Grid (Сетка)
Размещение по ячейкам (строки/колонки).
```python
widget.grid(row=0, column=1, sticky="w", padx=5)
# sticky: N, S, E, W, CENTER
```

### Place (Позиция)
Абсолютное позиционирование.
```python
widget.place(x=50, y=100, width=100, height=50)
```

## ⚡ События (Events)

### Bind (Привязка)
Реакция на действия пользователя.
```python
def on_click(event):
    print("Clicked at", event.x, event.y)

btn.bind("<Button-1>", on_click)  # ЛКМ
root.bind("<Return>", on_enter)   # Enter
root.bind("<Key>", on_key)        # Любая клавиша
```

### Command (Кнопки)
Простая привязка функции к действию.
```python
btn = tk.Button(root, text="Go", command=my_function)
```

## 🔗 Переменные (Variables)

Связь виджетов с данными (автоматическое обновление).

```python
var = tk.StringVar()
entry = tk.Entry(root, textvariable=var)

# Получить значение
val = var.get()
# Установить значение
var.set("New Text")
```
*Типы:* `StringVar`, `IntVar`, `BooleanVar`, `DoubleVar`.

## 🗨 Диалоги

### Messagebox
```python
from tkinter import messagebox

messagebox.showinfo("Title", "Text")
messagebox.showerror("Error", "Text")
res = messagebox.askyesno("Question", "Sure?")
```

### FileDialog
```python
from tkinter import filedialog

file = filedialog.askopenfilename()
folder = filedialog.askdirectory()
```

## ⛔ Частые ошибки

| ❌ Нельзя | ✅ Нужно |
| :--- | :--- |
| Забыть `mainloop()` | Всегда вызывать `root.mainloop()` |
| `time.sleep()` в GUI | `root.after(1000, func)` |
| Тяжелые задачи в потоке GUI | Использовать `threading` |
| Создавать виджеты в цикле без сохранения | Сохранять ссылки (список) |

## 🏁 Полный шаблон

```python
import tkinter as tk
from tkinter import ttk, messagebox

def on_click():
    name = entry.get()
    if not name:
        messagebox.showwarning("Warning", "Введите имя!")
        return
    messagebox.showinfo("Hello", f"Привет, {name}!")

root = tk.Tk()
root.title("My App")
root.geometry("300x200")

frame = ttk.Frame(root, padding=10)
frame.pack()

lbl = ttk.Label(frame, text="Ваше имя:")
lbl.grid(row=0, column=0, sticky="w")

entry = ttk.Entry(frame)
entry.grid(row=0, column=1, pady=5)

btn = ttk.Button(frame, text="OK", command=on_click)
btn.grid(row=1, column=1, sticky="e")

root.mainloop()
```