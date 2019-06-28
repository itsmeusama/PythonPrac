#Py Func takes a list and returns a new list with unique elements of the first list. 
def uniquel (ul):
    x = []
    for i in ul:
        if i not in x:
            x.append(i)
    return x

print(uniquel([1,2,3,1,2,4,5]))    