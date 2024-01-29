import tkinter as tk
import random

def on_button_click_one():
    label.config({game("Камінь")})
def on_button_click_two():
    label.config({game("Камінь")})
def on_button_click_three():
    label.config({game("Камінь")})
def game(player_choice):
    choices = ["Камінь", "Ножиці", "Папір"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        outcome = "Нічия"
    elif (player_choice == "Камінь" and computer_choice == "Ножиці") or (player_choice == "Ножиці" and computer_choice == "Папір") or (player_choice == "Папір" and computer_choice == "Камінь"):
        outcome = "Ти виграв!"
    else:
        outcome = "Ти програв"
    
    result = tk.Label(root, text = f"Твій вибір - {player_choice} \nВибір комп'ютера - {computer_choice}\nРезультат - {outcome}", font = ("Arial"))
    result.pack()
    pause = tk.Label(root, text=("---------------------------------"))
    pause.pack()


# Створення головного вікна
root = tk.Tk()
root.title("Камінь-Ножиці-Напір")


# Додавання елементів інтерфейсу

label = tk.Label(root, text="Вітаємо у грі - Камінь-Ножиці-Папір", font=("bold"))
label.pack()

button1 = tk.Button(root, text="Камінь", activebackground="red" ,command=on_button_click_one)
button1.pack()

button2 = tk.Button(root, text="Ножиці", activebackground="red", command=on_button_click_two)
button2.pack()

button3 = tk.Button(root, text="Папір", activebackground="red", command=on_button_click_three)
button3.pack()

label_log = tk.Label(root, text="Лог твоїх ігор", font=("Calibri 20 bold"))
label_log.pack()

# Запуск головного циклу
root.mainloop()