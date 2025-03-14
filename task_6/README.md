# Завдання 6: Жадібні алгоритми та динамічне програмування для вибору їжі

Цей проєкт реалізує два підходи до задачі вибору страв з найбільшою сумарною калорійністю в межах обмеженого бюджету:

1. **Жадібний алгоритм**, який вибирає страви, максимізуючи співвідношення калорій до вартості.
2. **Алгоритм динамічного програмування**, який обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

## Опис задачі

У нас є список страв з вказаною вартістю та калорійністю. Метою є вибрати такий набір страв, який максимально збільшить калорійність, не перевищуючи заданий бюджет.

```python
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
```

## Підходи до розв'язку

### 1. Жадібний алгоритм

Жадібний алгоритм вибирає страви, максимізуючи співвідношення калорій до вартості, поки не буде перевищено бюджет.

### 2. Динамічне програмування

Алгоритм динамічного програмування обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті. Алгоритм використовує масив для зберігання найбільших досягнутих результатів на кожному кроці.

## Вимоги

- **Python 3.x**
- **Бібліотека `matplotlib`** для побудови графіків (для демонстрації часу виконання алгоритмів)

## Інструкція з використання

1. Клонуйте або завантажте цей репозиторій.
2. Запустіть файл Python для виконання алгоритмів.

```bash
python main.py
```

## Приклад використання:

```bash
budget = 100  # Припустимо, що бюджет 100

greedy_result, greedy_calories = greedy_algorithm(budget)
dp_result, dp_calories = dynamic_programming(budget)

print(f"Жадібний алгоритм:")
for item, details in greedy_result.items():
    print(f"{item} (Вартість: {details['cost']}, Калорії: {details['calories']})")
print(f"Загальна калорійність: {greedy_calories}")

print("\nДинамічне програмування:")
for item in dp_result:
    print(f"{item} (Вартість: {items[item]['cost']}, Калорії: {items[item]['calories']})")
print(f"Загальна калорійність: {dp_calories}")
```

## Приклад виведення:

```bash
Жадібний алгоритм:
pizza (Вартість: 50, Калорії: 300)
hamburger (Вартість: 40, Калорії: 250)
Загальна калорійність: 550

Динамічне програмування:
pizza (Вартість: 50, Калорії: 300)
cola (Вартість: 15, Калорії: 220)
pepsi (Вартість: 10, Калорії: 100)
Загальна калорійність: 620
```

### Пояснення функцій

- greedy_algorithm(budget)
  Функція для жадібного алгоритму. Вибирає страви на основі максимального співвідношення калорій до вартості.

- dynamic_programming(budget)
  Функція для алгоритму динамічного програмування. Обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
