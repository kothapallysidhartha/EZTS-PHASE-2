# s=input()
# li=["{","(","["]
# stack=[]
# li2=["}",")","]"]
# d={}
# check=0
# opt="True"
# for i in range(0,len(s)-1):
#     if s[i] is in li:
#         d[s[i]]=li.index(s[i])
#         stack.append(s[i])
#     else:
#         e=stack.pop()
#         d[s[i]]=-1*li.index(e)
        
        
stack=[]
s=input()
n=len(s)-1
flag=0
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
    flag=0
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
            flag+=1
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
                flag-=1
            else:
                flag+=1
                break
        else:
            flag=-1
            break
    if flag==0:
        print(True)
    else:
        print(False)