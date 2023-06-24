stack=[]
def push():
    y=int(input("\nEnter the element:"))
    stack.append(y)
    display()
def pop():
    if not stack:
        print("\nStack is empty")
    else:
        e=stack.pop()
        print("\nRemoved an element:",e)
        display()
def display():
    print(stack)
    x=input()
while 1:
    x=int(input("\nSelect a option\n1.PUSH\n2.POP\n3.DISPLAY\n4.PEEK\n5.EXIT\nEnter:"))
    if x==1:
        push()
    elif x==2:
        pop()
    elif x==3:
        display()
    elif x==5:
        break
    elif x==4:
        if not stack:
            print("\nStack is empty")
            x=input()
        else:
            print(stack[len(stack)-1])
            x=input()
    else:
        print("\nEnter the correct input")