#String Reverse via Python Function

def reverse(s): 
    str = "" 
    for i in s: 
        str =  i + str 
    return str

s="hello"

print (reverse(s))