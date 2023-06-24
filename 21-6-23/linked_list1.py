class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print('Linked list is Empty!')
        else:
            temp=self.head
            while temp:
                print("->",temp.data,end=" ")
                temp=temp.next

    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
        
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        
        np.next=temp.next
        temp.next=np

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
        
    def delete_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def search_element(self):
        y=int(input("Enter search element:"))
        temp=self.head
        c=0
        while temp.next!=None:
            if temp.data==y:
                print("\nElement is found")
                c=1
                break
            temp=temp.next
        if c==0:
            print("\nElement not found")
    
    
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
obj.insert_beginning(500)
obj.insert_beginning(200)
print("\n------Insert_Begin-----")
obj.insert_end(1000)
print("\n------Insert_end-----")
obj.display()
print("\n------Delete_Position-----")
obj.display()
obj.delete_position(1)
print("\n------Delete_beg-----")
obj.display()
obj.delete()
obj.display()
print("\n------Del_end-----")
obj.delete_last()
obj.display()
print("\n------Search_element-----")
obj.search_element()
obj.display()
