# li=list(map(int,input().split(",")))
# k=int(input())
# li.sort()
# j=-1
# i=int(len(li)/2)
# while(i):
#     while j>=(-(len(li)/2)):
#         if li[i]+li[j]==k:
#             print("yes",li[i],li[j])
#         #print(li[i],li[j])
#         j=j-1
#     i=i-1


# i=0
# j=len(li)-1
# while(i<j):
#     if(li[i]+li[j]==k):
#         print("yes",li[i],li[j])
#         break
#     elif li[i]+li[j]>k:
#         j=j-1
#     else:
#         i=i+1

# A=[1,6,7,5,6,7,10]
# d={}
# for i in A:
#     if i not in d:
#         d[i]=1
# A=[]
# B=list(d.keys())
# print(B)


# d={}
# l=0
# for i in li:
#     if i not in d:
#         d[i]=1
# for i in li:
#     if k-i in d:
#         print("yes",i,k-i)
#         c=1
#         break
# if c==0:
#     print("no")

# s1=input()
# s2=input()
# d={}
# c=0
# for i in s1:
#     if i not in d:
#         d[i]=1
# s1=[]
# for i in s2:
#     if i in d and i not in s1:
#         c=1
#     s1.append(i)
# if c!=1:
#     print("no")
# else:
#     print(s1)