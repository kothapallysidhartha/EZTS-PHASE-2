#balance the parenthesis -"{}()[]"
li=["{","(","["]
b=["}",")","]"]
stack=[]
d={}
def ex(a,li):
    return li.index(a)
s=input()
if (s[0]=="}" or s[0]==")" or s[0]=="]") or len(s)%2!=0:
    print("Invalid syntax")
else:
    for i in range(0,len(s)):
        if s[i] in li:
            stack.append(s[i])
            gi=ex(s[i],li)
            d[s[i]]=b[gi]
        else:
            if s[i] in d.values():
                n=len(stack)-1
                if b.index(s[i])==li.index(stack[n]):
                    stack.pop()
                else:
                    break
    if not stack:
        print("Balanced")
    else:
        print("Not balanced")