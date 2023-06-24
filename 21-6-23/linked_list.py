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
    def insert_beginning(self):
        y=int(input("\nEnter no.of inputs to insert at begin:"))
        for i in range(0,y):
            data=int(input("Enter data:"))
            nb=Node(data)
            nb.next=self.head
            self.head=nb
        
        
    def insert_end(self,data):
        y=int(input("\nEnter no.of inputs to insert at end:"))
        for i in range(0,y):
            data=int(input("Enter data:"))
            ne=Node(data)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=ne
            ne.next=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
        


obj=singlelinkedlist()
obj.insert_beginning()
print("\n------Begin-----")
#obj.insert_beginning(200)
obj.insert_end(1000)
obj.display()
print("")
# obj.insert_position(1,186)
obj.display()