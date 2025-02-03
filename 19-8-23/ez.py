"""n=int(input("day:"))
match n:
    case 1:
        print("Monday")
        
    case 2:
        print("Tuesday")
        
    case 3:
        print("Wednesday")
        
    case 4:
        print("Thursday")
        
    case 5:
        print("Friday")
        
    case 6:
        print("Saturday")
        
    case 7:
        print("Sunday")
    case _:
        print("enter valid choice")"""

"""week=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
n=int(input("enter day:"))
for i in range(len(week)):
    if i+1 == n:
        print(week[i])"""
        
"""class abc:
    def a(self):
        print("method1")
    def b(self):
        print("method2")
l=abc()
l.a()
l.b()
class A:
    def A1(self):
        print("method A1")
    def A2(self):
        print("method A2")
class B(A):
    def B1(self):
        print("in B1")
obj=B()
obj.A1()
obj.A2()
obj.B1()
class A:
    def A1(self):
        print("method A1")
    def A2(self):
        print("method A2")
class B(A):
    def B1(self):
        print("in B1")
class C(B):
    def C1(self):
        print("in C1")
obj=C()
obj.A1()
obj.B1()
obj.C1()
class A:
    def A1(self):
        print("method A1")
    def A2(self):
        print("method A2")
class B:
    def B1(self):
        print("in B1")
class C(A,B):
    def C1(self):
        print("in C1")
obj=C()
obj.A1()
obj.B1()
obj.C1()
class A:
    def A1(self):
        print("method A1")
    def A2(self):
        print("method A2")
class B(A):
    def B1(self):
        print("in B1")
class C(A):
    def C1(self):
        print("in C1")
obj=C()
obj.C1()
obj.A1()
obj1=B()
obj1.A1()
obj1.B1()
#OVERLOADING
class greeting():
    def sum_of_elements(self,num1,num2):
        print("the sum of two elements are:",num1+num2)
    def sum_of_elements(self,num1,num2,num3):
        print("the sum of three elements are:",num1+num2+num3)
ob=greeting()
ob.sum_of_elements(1,2,3)
ob.sum_of_elements(1,2)"""
"""The function accepts an integers r of size 'length' as its arguments you are required to return the
sum of second largest element from the even positions and second smallest from
"""
"""li=list(map(int,input("").split(" ")))
el=li[0]
ol=li[1]
for i in range(len(li)):
    if i%2==0 :
        if li[i]>el:
            el=li[i]
    else:
        if li[i]<ol:
            ol=li[i]
li=[]
print(el+ol)"""

"""li1=list(input())
li2=list(input())
if len(li1)==len(li2):
    for i in li1:
        if i in li2:
            li2.remove(i)
    if len(li2)==0:
        print("is an anagram")
    else:
        print("Not a anagram")
else:
    print("Not a anagram")"""
li1=list(map(str,input().split(" ")))
li2=[]
for i in li1:
    l=len(i)
    for j in range(0,l):
        li2.append(i[j])
li2.sort()
l=len(li2)
while(l!=-1)
    print(li2[l],end=" ")
    l=l-1