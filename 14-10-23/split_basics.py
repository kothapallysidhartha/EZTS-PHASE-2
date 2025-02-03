# a=input()
# a=int(a)
# result=0
# y=1
# while(a):
#     if a>=100:
#         result=result+(100*y)
#         y+=1
#         a=a-100
#     elif a<100:
#         result=result+(a*y)
#         a=0
# print(result)

# a=int(input())
# h=a//3600
# m=(a%3600)//60
# s=((a%3600)%60)
# print(h,m,s)

# a=input()
# c=1
# p=0
# for i in range(len(a)-1):
#     if ord(a[i])+1==ord(a[i+1]):
#         c=c+1
#         if i==len(a)-1 and c>p:
#             p=c
#     elif c>p:
#         p=c
#         c=0
#     else:
#         c=0
# print(p)

A='A'
Z='Z'
a='a'
z='z'
li=['!','@','#','$','%','^','&','*','(',')','-','+']
new=[]
l=int(input())
paas=input()
c=0
q=0
Q=0
for i in paas:
    if (i in li): 
        c=c+1
    elif(i>=A and i<=Z):
        q+=1
    elif (i>=a and i<=z):
        Q+=1
    else:
        new.append(int(i))
if len(paas)<6:
    print(6-len(paas))
elif (c==0 or q==0 or Q==0) and len(paas)>=6:
    print("1")