class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("\nEMPTY LIST")
        else:
            temp=self.head
            print("NULL<----->",end=" ")
            while temp:
                if temp.next is not None:
                    print(temp.data,"<---->",end=" ")
                else:
                    print(temp.data,"<----->NULL",end=" ")
                temp=temp.next
    def insert_at_begin(self):
        y=int(input("\nEnter the the no.of inputs:"))
        for i in range(0,y):
            data=int(input("\nEnter data:"))
            new=Node(data)
            temp=self.head
            temp.prev=new
            new.next=temp
            self.head=new
    def insert_end(self):
        key=int(input('Enter the Data: '))
        n=Node(key)
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next 
        temp.next=n 
        n.prev=temp
    def insert_pos(self):
        pos=int(input('Enter the Position : '))
        data=int(input('Enter the Data : '))
        n=Node(data)
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next 
        n.previous=temp
        n.next=temp.next
        temp.next.previous=n 
        temp.next=n
    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp2=temp.prev
        temp2.next=None
        temp.prev=None
    def delete_pos(self):
        pos=int(input('Enter the Position:'))
        temp=self.head.next
        previous=self.head
        for i in range(1,pos-1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next
        temp.next=None
        
obj=dll()
n1=Node(120)
obj.head=n1
n2=Node(910)
n2.prev=n1
n1.next=n2
n3=Node(996)
n3.prev=n2
n2.next=n3
n3.next=None
obj.display()
print("\nInsertion\nInsetion at begin\n")
obj.insert_at_begin()
obj.display()
print("\nInsertion\nInsetion at end\n")
obj.insert_end()
obj.display()
print("\nInsertion\nInsetion at position\n")
obj.insert_pos()
obj.display()
print("\nDeletion\nDeletion at begin\n")
obj.delete_beg()
obj.display()
print("\nDeletion\nDeletion at end\n")
obj.delete_end()
obj.display()
print("\nDeletion\nDeletion at position\n")
obj.delete_pos()
obj.display()