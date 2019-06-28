#Finding Max from 3 Numbers

def Maximum(x,y,z):

    if(x >= y) and (x >= z):
        largest = x

    elif (y >= z) and (x >= x):
        largest = y
    else:
        largest = z
        return largest  

print (Maximum(5,10,15))