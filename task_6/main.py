items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(budget):
    # Рахуємо співвідношення калорій до вартості
    ratio = [(item, value['calories'] / value['cost']) for item, value in items.items()]
    ratio.sort(key=lambda x: x[1], reverse=True)  # Сортуємо за зменшенням співвідношення калорій до вартості

    result = {}
    total_cost = 0
    total_calories = 0

    for item, _ in ratio:
        cost = items[item]['cost']
        calories = items[item]['calories']
        if total_cost + cost <= budget:
            result[item] = {'cost': cost, 'calories': calories}
            total_cost += cost
            total_calories += calories

    return result, total_calories

# Динамічне програмування
def dynamic_programming(budget):
    # dp[i] — максимальна кількість калорій, яку можна отримати з бюджетом i
    dp = [0] * (budget + 1)
    # Для відновлення результату
    chosen_items = [[] for _ in range(budget + 1)]

    for item, value in items.items():
        cost = value['cost']
        calories = value['calories']
        for i in range(budget, cost - 1, -1):
            if dp[i - cost] + calories > dp[i]:
                dp[i] = dp[i - cost] + calories
                chosen_items[i] = chosen_items[i - cost] + [item]

    # Повертаємо оптимальний набір страв для максимізації калорій
    return chosen_items[budget], dp[budget]

# Приклад використання
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
