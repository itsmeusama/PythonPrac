
def checkpassword(guess, password):
    

    
    if guess == password:
        print ("good job!")
        exit(1)
    else:
        print ("password not match")


def vault(password):
    attempt = 1
    while attempt < 4:
        guess = input("Make your guess: ")
        checkpassword(guess, password)
        attempt += 1

    print ("sorry too many trys...")

if __name__ == '__main__':
    print ("User, enter your password por favor: ")
    password = input()
    vault(password)