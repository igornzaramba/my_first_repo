ls=[10, 2, 7,23, 5,11,15]

arr = ls

n = len(ls)

for i in range (n):
    flag = False

    for j in range (0, n-i-1):

        if arr[j]>ls[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = True
        
    if flag == True:
        break

print('initial array:',ls)
print('sorted array:',arr)
