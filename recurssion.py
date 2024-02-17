import math
fact = int(input('Plase input a number:'))

def recursion(fact):
   n= math.factorial(fact)

   return(n)

number = recursion(fact)

print ('n!=',number)