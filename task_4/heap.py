import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Додає елемент в купу і коригує її структуру."""
        self.heap.append(val)  # Додаємо елемент в кінець
        self._heapify_up(len(self.heap) - 1)  # Виправляємо структуру купи

    def _heapify_up(self, index):
        """Просуває елемент вгору по купі до правильного місця."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Якщо поточний елемент менший за батьківський, міняємо їх місцями
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Рекурсивно коригуємо структуру до самого кореня
            self._heapify_up(parent_index)

    def build_heap(self):
        """Перебудовує купу за допомогою алгоритму 'heapify'."""
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        """Просуває елемент вниз по купі до правильного місця."""
        smallest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        if smallest != index:
            # Якщо найменший елемент не поточний, міняємо їх місцями
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # Рекурсивно коригуємо структуру
            self._heapify_down(smallest)

    def build_tree(self):
        """Будує дерево з поточної купи для візуалізації."""
        nodes = []
        for val in self.heap:
            nodes.append(Node(val))
        for i in range(len(self.heap)):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(self.heap):
                nodes[i].left = nodes[left_index]
            if right_index < len(self.heap):
                nodes[i].right = nodes[right_index]
        return nodes[0]  # Повертаємо корінь дерева

