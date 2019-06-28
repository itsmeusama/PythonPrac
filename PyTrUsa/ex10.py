#Py func that takes a number as a parameter and check the number is prime or not. 
def primechecker(num):
    
    if(num <= 1):
        return False
    
    elif(num == 2):
        return True
    else:
        for x in range(2,num):
            if(num%x==0):
                return 'Non Prime'
    return 'Prime'
print(primechecker(9))    