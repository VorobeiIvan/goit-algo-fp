# Клас Node для представлення вузла списку
class Node:
    def __init__(self, data=None):
        self.data = data  # Значення даних у вузлі
        self.next = None  # Посилання на наступний вузол
