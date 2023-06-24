class Node:
    def _init_(self,key):
        self.key=key
        self.left=None
        self.right=None 
    
    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.key,end='')
            inorder(root.right)
            
    def insert(node,key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left =insert(node.left,key)
        else:
            node.right =insert(node.right,key)
        return node
            
def minValueNode(node):
    current=node
    while(current.left is not None):
        current = current.left 
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left = deleteNode(root.left,key)
    elif (key > root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp =root.right
            root =None
            return temp 
        elif root.right is None:
            temp=root.left
            root =None
    temp=minvalueNode(root.right)
    root.key=temp.key
    root.right=deleteNode(root.right,temp.key)
return root
root=None
root=insert(root,50)
root=insert(root,3)
root=insert(root,80)
root=insert(root,120)
root=insert(root,950)
root=insert(root,681)
print("\ninorder")
inorder(root)
print("\ndelete 80")
root=deleteNode(root,80)
print("Inorder :modified tree\n")
inorder(root)
root=deleteNode(root,120)
print("Inorder :modified tree\n")
inorder(root)
