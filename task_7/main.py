import numpy as np
import matplotlib.pyplot as plt

# Функція для моделювання кидків двох кубиків
def roll_dice(num_rolls):
    dice_rolls = np.random.randint(1, 7, (num_rolls, 2))  # Кидаємо два кубики
    sums = np.sum(dice_rolls, axis=1)  # Обчислюємо суму кожного кидка
    return sums

# Ініціалізація
num_rolls = 100000  # Кількість кидків кубиків
sums = roll_dice(num_rolls)

# Підрахунок кількості кожної можливої суми
sum_counts = np.zeros(11)  # Можливі суми: від 2 до 12 (всього 11 значень)
for sum_value in sums:
    sum_counts[sum_value - 2] += 1

# Обчислення ймовірності для кожної суми
probabilities = sum_counts / num_rolls

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Виведення таблиці з ймовірностями в відсотках з вертикальними розділеннями
print(f"{'Сума':<6} | {'Метод Монте-Карло':<25} | {'Аналітична'}")
print('-' * 60)
for sum_value in range(2, 13):
    monte_carlo_percentage = probabilities[sum_value - 2] * 100
    analytical_percentage = analytical_probabilities[sum_value] * 100
    print(f"{sum_value:<6} | {monte_carlo_percentage:>8.2f}% ({int(num_rolls * probabilities[sum_value - 2])} разів на {num_rolls} кидків) | "
          f"{analytical_percentage:>8.2f}% ({int(num_rolls * analytical_probabilities[sum_value])} разів на {num_rolls} кидків)"
)

# Побудова графіка
x = np.arange(2, 13)  # Можливі суми
plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, probabilities, width=0.4, label='Монте-Карло', color='blue', alpha=0.7)
plt.bar(x + 0.2, [analytical_probabilities[i] for i in x], width=0.4, label='Аналітичні', color='red', alpha=0.7)

plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність')
plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
plt.xticks(x)
plt.legend()

# Виведення графіка
plt.show()
