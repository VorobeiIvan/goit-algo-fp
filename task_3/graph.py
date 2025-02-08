class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Кількість вершин
        self.edges = {i: [] for i in range(vertices)}  # Словник для збереження ребер

    def add_edge(self, u, v, weight):
        # Додаємо ребро до графа (орієнтований граф)
        self.edges[u].append((v, weight))

    def get_neighbors(self, u):
        # Повертаємо сусідів вершини u
        return self.edges[u]
