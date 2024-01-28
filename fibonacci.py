count=int(input('Count for Fibonacci count:'))
ind = 1
print('The Fibonacci sequence is as follow:')
if count == 0:

    print(0)

else: 
    x1 = 0
    x2 = 1
    print(x1)
    print(x2)

    while ind < count :
        Fibonacci = x1 + x2
        print (Fibonacci)
        x1=x2
        x2=Fibonacci
        ind+=1
 

