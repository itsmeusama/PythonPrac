import time
# get pass To Hide The Characters
from getpass import getpass

PASSWORD = 'hello123'
guess = 1
is_out_of_guess = False

while is_out_of_guess == False:

    inppwd = getpass('Type Yo Password: ')
    if inppwd == PASSWORD:
        print('You re Login in.....')
        break
    elif inppwd != PASSWORD and guess < 3:
        print('You have entered a wrong password')
    else:
        print('You re out of chances Pls Wait for 10 Sec')
        time.sleep(10)
        guess = 0
        continue
        print('Now Try')
    guess += 1
