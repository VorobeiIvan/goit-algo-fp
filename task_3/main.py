from graph import Graph
from dijkstra import dijkstra

def get_graph_input():
    # Введення кількості вершин
    vertices = int(input("Введіть кількість вершин: "))
    graph = Graph(vertices)

    # Введення кількості ребер
    edges_count = int(input("Введіть кількість ребер: "))
    
    # Цикл для введення кожного ребра
    for i in range(1, edges_count + 1):
        print(f"Введіть ребро {i} у форматі 'вихідна вершина, вхідна вершина, вага':")
        u, v, weight = map(int, input().split(','))
        graph.add_edge(u, v, weight)

    return graph


def main():
    # Отримуємо граф і початкову вершину від користувача
    graph = get_graph_input()

    start = int(input("Введіть початкову вершину для обчислення найкоротших шляхів: "))
    distances = dijkstra(graph, start)

    # Виводимо найкоротші шляхи
    print(f"Найкоротші шляхи від вершини {start}:")
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {distance}")

if __name__ == "__main__":
    main()
