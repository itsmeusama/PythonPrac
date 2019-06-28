#Write a Python function that accepts a string and calc the no.of upper case and lower case letters.
#method1
def casechecker(str):
    upper=0
    lower=0
    for i in range (len(str)):
        if(i.isupper()):
            upper+=1
        elif(i.islower()):
            lower+=1

str = 'HellOMM'
casechecker(str)
#print(casechecker('HellO'))
print("No of UpperCase Values are: ", upper)
print("No of LowerCase Values are: ",lower)