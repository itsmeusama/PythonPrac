#Write a Python program to print the even numbers from a given list. 

def displayeven(numlist):
    for i in range(0,len(numlist)):
        if(numlist[i]%2 == 0):
            print(numlist[i])
        else:
            pass

num = [12,15,5,10,3]
print(displayeven(num))
