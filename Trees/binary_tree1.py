class Node:  # Class name should be capitalized
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(node):  # Function name is fine, but ensure 'Node' is used in class
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

# Taking input and constructing the tree
k = int(input("Enter root value: "))
root = Node(k)  # Use 'Node' instead of 'node'

k = int(input("Enter left child value: "))
root.left = Node(k)

root.right = Node(int(input("Enter right child value: ")))

root.left.left = Node(int(input("Enter left-left child value: ")))
root.left.right = Node(int(input("Enter left-right child value: ")))

root.right.left = Node(int(input("Enter right-left child value: ")))
root.right.right = Node(int(input("Enter right-right child value: ")))

print("Preorder Traversal:")
pre_order(root)
