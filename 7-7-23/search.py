#linear search
li=[]
s=int(input("Enter size:"))
for i in range(s):
    k=int(input("\nEnter an element:"))
    li.append(k)
key=int(input("\nEnter search element:"))
li.sort()
start=0
end=len(li)-1
mid=int((end-start)/2)
f=0
while mid!=start or mid!=end:
    if li[mid]==key:
        print("\n Search element is found at index {}".format(li.index(key)))
        f=1
        break
    elif li[mid]>key:
        start=li.index(li[mid])-1
    elif li[mid]<key:
        end=li.index(li[mid])+1
if f==0:
    print("\nNo element is found")