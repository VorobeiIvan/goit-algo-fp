from heap import MinHeap
from visualization import draw_tree
from utils import dfs, bfs

def user_interface():
    heap = MinHeap()
    print("Програма для роботи з мін-купою: додавання, перегляд та візуалізація.")

    menu = ("\nОберіть одну з опцій:\n"
            "1. Додати числа в мін-купу\n"
            "2. Показати мін-купу\n"
            "3. Вихід")

    print(menu)
    
    while True:
        option = input("\nВведіть номер опції: ")
        
        if option == '1':
            numbers = input("Введіть числа (через пробіл, наприклад, '1 15 4 0') або 'q' для виходу: ")
            if numbers.strip().lower() == 'q':
                continue
            try:
                for num in numbers.split():
                    heap.insert(int(num))
                    print(f"Число {num} додано в купу.")
            except ValueError:
                print("Некоректне введення! Введіть лише числа через пробіл.")
        
        elif option == '2':
            if heap.is_empty():
                print("Купа порожня. Спочатку додайте числа.")
                continue
            
            print("Побудова мін-купи...")
            heap.build_heap()
            tree_root = heap.build_tree()
            draw_tree(tree_root, title="Мін-купа")
            
            print("\nОбхід дерева в глибину (DFS):")
            dfs_result = dfs(tree_root)
            if dfs_result:
                print(" -> ".join(map(str, dfs_result)))
            else:
                print("Помилка: обхід DFS не повернув значення.")
            draw_tree(tree_root, title="Обхід дерева в глибину (DFS)")
            
            print("\nОбхід дерева в ширину (BFS):")
            bfs_result = bfs(tree_root)
            if bfs_result:
                print(" -> ".join(map(str, bfs_result)))
            else:
                print("Помилка: обхід BFS не повернув значення.")
            draw_tree(tree_root, title="Обхід дерева в ширину (BFS)")
        
        elif option == '3':
            print("Завершення роботи програми.")
            break
        
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    user_interface()
