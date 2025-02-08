# -*- coding: utf-8 -*-
import os
import subprocess

def list_tasks():
    return [d for d in os.listdir() if os.path.isdir(d) and d.startswith("task_")]

def run_task(task_name):
    task_path = os.path.join(task_name, "main.py")
    if os.path.exists(task_path):
        subprocess.run(["python", task_path])
    else:
        print(f"[Помилка] У директорії {task_name} немає main.py")

def main():
    while True:
        tasks = list_tasks()
        print("\n=== Меню завдань ===")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("0. Вихід")

        choice = input("Оберіть номер завдання для запуску: ")
        if choice == "0":
            print("Вихід...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(tasks):
            run_task(tasks[int(choice) - 1])
        else:
            print("[Помилка] Некоректний вибір!")

if __name__ == "__main__":
    main()
