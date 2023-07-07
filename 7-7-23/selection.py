#finding min index and swapping with current element to right
a= [6,9,7,2,5]
size = len(a)
for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if a[j] < a[min_index]:
                min_index = j
        (a[i], a[min_index]) = (a[min_index], a[i])
print('The array after sorting by selection sort is:')
print(a)