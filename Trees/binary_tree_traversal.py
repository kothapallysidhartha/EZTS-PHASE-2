class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

k = int(input("Enter root value: "))
root = Node(k)  # Use 'Node' instead of 'node'

k = int(input("Enter left child value: "))
root.left = Node(k)

root.right = Node(int(input("Enter right child value: ")))

root.left.left = Node(int(input("Enter left-left child value: ")))
root.left.right = Node(int(input("Enter left-right child value: ")))

root.right.left = Node(int(input("Enter right-left child value: ")))



print("Preorder Traversal:")
pre_order(root)
print("Inorder Traversal:")
inorder(root)
print("Postorder Traversal:")
post_order(root)