class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.key = key

def height(root):
    if root is None:
        return -1  # If counting edges; return 0 if counting nodes
    return 1 + max(height(root.left), height(root.right))

# Example Usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))  # Output: 2 (height in terms of edges)
