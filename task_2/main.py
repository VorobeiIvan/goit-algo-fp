import tkinter as tk
from tkinter import simpledialog, messagebox
import turtle
import math

# Функція для малювання дерева Піфагора
def pythagoras_tree(t, length, level):
    if level == 0:
        return
    else:
        t.forward(length)
        t.left(45)
        pythagoras_tree(t, length / math.sqrt(2), level - 1)
        t.right(90)
        pythagoras_tree(t, length / math.sqrt(2), level - 1)
        t.left(45)
        t.backward(length)

# Функція для створення вікна з описом
def show_description():
    description = """Дерево Піфагора — це фрактал, який будується шляхом рекурсивного додавання нових гілок.
У цьому застосунку ви можете вказати рівень рекурсії, і програма побудує дерево відповідно до вашого вибору.
Чим вищий рівень рекурсії, тим більше гілок на дереві, і воно стає складнішим."""
    messagebox.showinfo("Опис", description)

# Функція для завершення малювання дерева та запит на повтор
def on_drawing_complete():
    response = messagebox.askyesno("Готово!", "Малювання завершено! Бажаєте намалювати інше дерево?")
    if response:
        draw_tree()  # Перезапускаємо малювання
    else:
        turtle.bye()  # Закриваємо черепаху

# Функція для запуску фрактала
def draw_tree():
    try:
        level = int(simpledialog.askstring("Введіть рівень рекурсії", "Введіть рівень рекурсії (наприклад, 5):"))
        if level < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректний рівень рекурсії (ціле число більше 0).")
        return
    
    # Створюємо нове вікно для малювання
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Налаштування розміру вікна для коректного відображення
    window.setup(width=800, height=600)  # Встановлюємо розмір вікна
    window.setworldcoordinates(-250, -150, 250, 300)  # Налаштуємо координатну систему для кращого вигляду
    
    t = turtle.Turtle()
    t.left(90)  # Початковий кут
    t.speed(0)  # Максимальна швидкість малювання
    t.color("red")  # Встановлюємо колір черепахи на червоний
    
    # Малюємо дерево Піфагора
    initial_length = 150  # Початкова довжина гілки
    pythagoras_tree(t, initial_length, level)
    
    # Завершення малювання та запит на повтор
    on_drawing_complete()

# Основне вікно застосунку
def main():
    root = tk.Tk()
    root.title("Дерево Піфагора")

    # Створюємо меню
    menubar = tk.Menu(root)
    
    # Додаємо меню "Файл"
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Вийти", command=root.quit)
    menubar.add_cascade(label="Файл", menu=file_menu)
    
    # Додаємо меню "Довідка"
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Опис", command=show_description)
    menubar.add_cascade(label="Довідка", menu=help_menu)
    
    root.config(menu=menubar)

    # Додаємо кнопку для малювання дерева
    draw_button = tk.Button(root, text="Малювати дерево", command=draw_tree)
    draw_button.pack(pady=20)

    # Додаємо опис
    label = tk.Label(root, text="Цей застосунок малює фрактал 'дерево Піфагора' з вказаним рівнем рекурсії.")
    label.pack(pady=10)

    # Запускаємо основне вікно
    root.mainloop()

# Запуск застосунку
if __name__ == "__main__":
    main()
