#Write a Python function to check whether a number is in a given range

def checkrange (num):
    if num in range(3,9):
        print(num,"is in the given range")
    else:
        print(num,'is Not in the given range')

checkrange(10)
