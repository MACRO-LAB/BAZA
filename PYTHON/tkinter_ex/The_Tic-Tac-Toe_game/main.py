from tkinter import Tk,messagebox,Button


root = Tk()
root.title("Крестики-нолики")
root.iconbitmap("icon1.ico")
current_player = "X"

def reset_game():
    global current_player
    current_player = "X"
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")


def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
    if check_winner():
        if messagebox.askyesno("Победа!", f"Победил {current_player}!\nИграть заново?"):
            reset_game()
    elif all(btn["text"] != "" for btn in buttons):
        [btn.config(bg="lightyellow") for btn in buttons]
        if messagebox.askyesno("Ничья!", "Игра окончена. Ничья!\nИграть заново?"):
            reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"


def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
        [0, 4, 8], [2, 4, 6]  # Диагональные линии
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            [buttons[win].config(bg="lightgreen") for win in combo]
            return True
    return False


buttons = []
for i in range(9):
    button = Button(
        root,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)



root.mainloop()
