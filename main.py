# -*- coding: utf-8 -*-
import os
import subprocess

# Функція для отримання списку завдань та сортування їх
def list_tasks():
    tasks = [d for d in os.listdir() if os.path.isdir(d) and d.startswith("task_")]
    return sorted(tasks)  # Сортуємо завдання за їх іменами

# Функція для запуску конкретного завдання
def run_task(task_name):
    task_path = os.path.join(task_name, "main.py")
    if os.path.exists(task_path):
        print(f"Запуск {task_name}...")
        subprocess.run(["python3", task_path])
    else:
        print(f"[Помилка] У директорії {task_name} немає main.py")

# Функція для виведення інформації про завдання
def show_task_info(task_name):
    task_descriptions = {
        "task_1": "Структури даних. Сортування. Робота з однозв'язним списком",
        "task_2": "Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії",
        "task_3": "Дерева, алгоритм Дейкстри",
        "task_4": "Візуалізація піраміди",
        "task_5": "Візуалізація обходу бінарного дерева",
        "task_6": "Жадібні алгоритми та динамічне програмування",
        "task_7": "Використання методу Монте-Карло"
    }
    print(f"Інформація про завдання {task_name}: {task_descriptions.get(task_name, 'Невідома інформація')}")

# Функція для відображення списку завдань з їх описами
def display_task_menu():
    tasks = list_tasks()
    print("\n=== Меню завдань ===")
    task_descriptions = {
        "task_1": "Структури даних. Сортування. Робота з однозв'язним списком",
        "task_2": "Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії",
        "task_3": "Дерева, алгоритм Дейкстри",
        "task_4": "Візуалізація піраміди",
        "task_5": "Візуалізація обходу бінарного дерева",
        "task_6": "Жадібні алгоритми та динамічне програмування",
        "task_7": "Використання методу Монте-Карло"
    }
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task_descriptions.get(task, 'Невідома інформація')}")
    print("0. Вихід")

# Основна функція
def main():
    while True:
        display_task_menu()
        
        choice = input("Оберіть номер завдання для запуску: ")
        tasks = list_tasks()
        
        if choice == "0":
            print("Вихід...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(tasks):
            selected_task = tasks[int(choice) - 1]
            show_task_info(selected_task)  # Виведення інформації про вибране завдання
            run_task(selected_task)  # Запуск вибраного завдання
        else:
            print("[Помилка] Некоректний вибір!")

# Перевірка запуску програми
if __name__ == "__main__":
    main()
