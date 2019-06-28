#Sum of the List Values

def sumofall(numlst):
    total=0
    for ele in range(len(numlst)):
        total = total + numlst[ele]
    return total

numlst = [10,20,30,40]
print (sumofall(numlst))

#Using 'Sum(list)' is the easiest way