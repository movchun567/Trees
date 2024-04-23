from collections import deque

def tree_by_levels(node):
    if node is None:
        return []
    queue = deque([node])
    levels = []
    while queue:
        len_ = len(queue)
        curr = []
        for _ in range(len_):
            node = queue.popleft()
            curr.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.extend(curr)
    return levels
