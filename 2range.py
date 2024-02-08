
num = int(input("Enter a number: "))
i=1

if num < 2:
   print("Sorry, the provided number is smaller than 2")

else:
   while i<num:

      flag = False

      if i == 1:
         pass
      elif i > 1:

         for ind in range(2,i):
            if (i % ind) == 0:
               flag = True
               break
         if flag:
            pass
         else:
            print(i, "is a prime number")

      i+=1
            

                
               
    
           
                
