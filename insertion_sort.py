arr=[12, 11, 13, 5, 6]

n= len(arr)

for i in range (1,n):
    key = arr[i]
    j = i-1
    while j>= 0 and key < arr[j]:
         arr[j+1] = arr[j]  # Shift elements to the right
         j -= 1
    arr[j+1] = key  # Insert the key in the correct position

print(arr)