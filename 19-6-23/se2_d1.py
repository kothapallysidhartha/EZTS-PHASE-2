n=1
while n==1:
    a=int(input("Enter the size:"))
    if a>=0:
        n=2
li=[]
n=-1
for i in range(0,a):
    el=int(input("Enter element:"))
    li.append(el)
while(n!=0):
    c=int(input("1.INSERTION\n2.DELETION\n3.SORT\n4.SEARCH\n5.EXIT\nENTER CHOICE:"))
    if c>5:
        print("incorrect choice")
    else:
        if c==5:
            li=[]
            n=0
        elif(c>=0 and c<5):
            if c==1:
                n=1
                while n==1:
                    a=int(input("Enter the size:"))
                    if a>=0:
                        n=2
                for i in range(0,a):
                    el=int(input("Enter element:"))
                    li.append(el)
            print(li)
        elif c==2:
            el=int(input("Enter the element:"))
            li.remove(el)
            print(li)
        elif c==3:
            li.sort()
            print(li)
        else:
            print(li)
            el=int(input("Enter the element:"))
            f=-1
            for i in li:
                if el==i:
                    f=1
                else:
                    f=0
            if f==1:
                print(el," found")
            else:
                print(el," not found in the list")
                
"""establish links
    by default every nodes next is null"""
