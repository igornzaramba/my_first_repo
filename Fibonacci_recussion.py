def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)

count = int(input('Count for Fibonacci count:'))
print('The Fibonacci sequence is as follow:')
for i in range(count):
    print(recur_fibonacci(i))