import webbrowser
import time

#App/script-which Remind user to take necessary interval time to time, here a video song will be played after certain interval (Time is provide below-make it minimal to check the prgrm) 
#interval periods are very miniml due to testing purposes


# count determined the no of times you need to take break
count = 3

while count > 0:

	#Certain action (Playing a video) will take place every 10 sec as time.sleep=10
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=vNLZAmLqibo")
    count -= 1
