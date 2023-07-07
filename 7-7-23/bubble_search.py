a=[2,7,5,9,8]
n=len(a)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            swap=True
            a[j],a[j+1]=a[j+1],a[j]
    if swap==False:
        break
print(a)