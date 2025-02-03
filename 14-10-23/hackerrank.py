def decryptPassword(s):
    # Write your code here
    #resultf=""
    num=""
    t=""
    for i in range(len(s)-1):
        if (s[i]>='a' and s[i]<='z') and (s[i+1]>='A' and s[i+1]<='Z'):
            t=s[i]
            s[i]=s[i+1]
            s[i+1]=t
            s[0]=t
            #resultf.append(s)
            t=""
        elif int(s[i])>=0 and int(s[i])<=9:
            num.append(s[i])
            s[i]=0 
    num.append(s)
    return num
s = input()
result = decryptPassword(s)
print(result)