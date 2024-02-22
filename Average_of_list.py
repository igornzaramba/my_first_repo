
def average(lst):

    if lst:
        
        total = sum(lst)
        
        count = len(lst)
        
        return total / count
    else:
    
        return None


numbers = [10, 20, 30, 40, 50]

print(average(numbers))
