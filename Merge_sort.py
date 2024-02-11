ls=[10, 2, 7,23, 5,11,15,890,93,773,837,27,24,44,90]

lenght = len(ls)
n=int(lenght/2)

arr1=ls[0:n]
k=len(arr1)


arr2=ls[-(n+1):]
l=len(arr2)


for i in range (k):
    flag1 = False

    for j in range (0, k-i-1):

        if arr1[j]>arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
            flag = True
        
    if flag1 == True:
        break

for ind in range (l):
    flag2 = False

    for p in range (0, l-ind-1):

        if arr2[p]>arr2[p+1]:
            arr2[p], arr2[p+1] = arr2[p+1], arr2[p]
            flag = True
        
    if flag2 == True:
        break

arr = arr1 + arr2

print('initial array:',ls)
print('sorted array:',arr)
