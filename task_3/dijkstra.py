import heapq

def dijkstra(graph, start):
    # Відстані від початкової вершини
    distances = {i: float('inf') for i in range(graph.vertices)}
    distances[start] = 0

    # Використовуємо мінімальну купу для вибору наступної вершини з найменшою відстанню
    pq = [(0, start)]  # (відстань, вершина)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Якщо поточна відстань більше знайденої, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо всіх сусідів
        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight

            # Якщо знайдений коротший шлях, оновлюємо відстань і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
