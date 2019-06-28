#Write a Python function that accepts a string and calc the no.of upper case and lower case letters.
#method2
def string_test(s):
    d={'Upper Case':0,'Lower Case':0}
    for i in d():
        if i.isupper():
            d['Upper Case'] += 1 
        elif i.islower():
            d['Lower Case'] += 1
        else:
            pass

print("No of upper case letters: ", d["Upper Case"])

print("No of lower case letters: ", d["Lower Case"])
print(string_test('HelloWorld'))