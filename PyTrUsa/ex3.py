#Py Function to multiply all the elements in a list

def multi(numlist):
    result=1
    for ele in numlist:
        result = result * ele
    return result


numlst = [2,3,4,5]
print(multi(numlst))