import webbrowser
import time

#App/script-which Remind user to take necessary interval time to time 

# no of times you need to take a break

count = 3

while count > 0:
    # stop the execution for 10sec
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=vNLZAmLqibo")
    count -= 1
