
num = int(input("Enter a number: "))

if num < 2:
   print("Sorry, the provided number is smaller than 2")

else:
   print(2)
   for ind in range(2, num +1):
      if ind > 1:
         for i in range(2,ind):
            if (ind % i) == 0:
               break
            else:
               print(ind)
            break
   
   

                

            
            

                
               
    
           
                