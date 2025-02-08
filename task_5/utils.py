def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    result = []
    step = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color = f"#{hex(255 - step * 5)[2:].zfill(2)}96F0"  # зміна кольору від темного до світлого
            step += 1
            result.append(node.val)  # Додаємо значення вузла у результат
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return result  # Повертаємо обхідний список

def bfs(tree_root):
    from collections import deque

    queue = deque([tree_root])
    visited = set()
    result = []
    step = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node.color = f"#{hex(255 - step * 5)[2:].zfill(2)}96F0"  # зміна кольору від темного до світлого
            step += 1
            result.append(node.val)  # Додаємо значення вузла у результат
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result  # Повертаємо обхідний список
