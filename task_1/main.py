from linked_list import LinkedList, merge_and_sort_lists

def input_numbers_for_list():
    while True:
        try:
            user_input = input("Введіть числа для списку через пробіл: ")
            numbers = list(map(int, user_input.split()))
            return numbers
        except ValueError:
            print("[Помилка] Будь ласка, введіть лише ціле число, розділене пробілами.")

# Головне меню
list1 = LinkedList()
list2 = LinkedList()
merged_list = LinkedList()

while True:
    print("\n=== Меню ===")
    print("1. Додати елементи до списку")
    print("2. Вивести список")
    print("3. Реверсувати список")
    print("4. Відсортувати список за допомогою сортування вставками")
    print("5. Об'єднати два списки")
    print("6. Вийти")
    option = input("Виберіть опцію: ")

    if option == "1":
        list_number = input("Який список ви хочете оновити? (1 або 2): ")
        if list_number == "1":
            numbers = input_numbers_for_list()
            list1.from_list(numbers)
        elif list_number == "2":
            numbers = input_numbers_for_list()
            list2.from_list(numbers)
        else:
            print("[Помилка] Некоректний вибір списку.")

    elif option == "2":
        list_number = input("Який список ви хочете вивести? (1, 2 або 3): ")
        if list_number == "1":
            print("Список 1: ")
            list1.print_list()
        elif list_number == "2":
            print("Список 2: ")
            list2.print_list()
        elif list_number == "3":
            print("Об'єднаний список: ")
            merged_list.print_list()
        else:
            print("[Помилка] Некоректний вибір списку.")

    elif option == "3":
        list_number = input("Який список ви хочете реверсувати? (1, 2 або 3): ")
        if list_number == "1":
            list1.reverse()
            print("Список 1 після реверсування: ")
            list1.print_list()
        elif list_number == "2":
            list2.reverse()
            print("Список 2 після реверсування: ")
            list2.print_list()
        elif list_number == "3":
            merged_list.reverse()
            print("Об'єднаний список після реверсування: ")
            merged_list.print_list()
        else:
            print("[Помилка] Некоректний вибір списку.")

    elif option == "4":
        list_number = input("Який список ви хочете відсортувати? (1, 2 або 3): ")
        if list_number == "1":
            list1.insertion_sort()
            print("Список 1 після сортування: ")
            list1.print_list()
        elif list_number == "2":
            list2.insertion_sort()
            print("Список 2 після сортування: ")
            list2.print_list()
        elif list_number == "3":
            merged_list.insertion_sort()
            print("Об'єднаний список після сортування: ")
            merged_list.print_list()
        else:
            print("[Помилка] Некоректний вибір списку.")

    elif option == "5":
        print("Об'єднання двох списків...")
        merged_list = merge_and_sort_lists(list1, list2)
        print("Об'єднаний відсортований список:")
        merged_list.print_list()

    elif option == "6":
        print("Вихід...")
        break

    else:
        print("[Помилка] Некоректний вибір.")
