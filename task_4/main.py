from heap import MinHeap
from visualization import draw_tree

if __name__ == "__main__":
    # Створюємо мін-купу
    heap = MinHeap()

    print("Вітаємо у програмі для візуалізації мін-купи!")
    print("Введіть числа для додавання в купу через пробіл. Для завершення введіть 'q'.")

    while True:
        # Отримуємо введення користувача
        user_input = input("Введіть числа (через пробіл) або 'q' для виходу: ")
        
        if user_input.lower() == 'q':
            print("Вихід з програми...")
            break
        
        try:
            # Якщо введено числа через пробіл
            numbers = user_input.split()
            for num in numbers:
                # Перетворюємо кожне значення на ціле число і додаємо в купу
                val = int(num)
                heap.insert(val)
                print(f"Число {val} додано в купу.")
        except ValueError:
            print("Будь ласка, введіть коректні числа, розділені пробілами, або 'q' для виходу.")
    
    # Після того, як усі числа додано в купу, застосовуємо перебудову купи
    heap.build_heap()

    # Створення дерева з купи
    root = heap.build_tree()

    # Відображення дерева
    draw_tree(root)
