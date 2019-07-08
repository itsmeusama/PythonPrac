import turtle 

star = turtle.Turtle()
star.pencolor("Blue")  #Coloured Line - Pencolor

for i in range(50):
    star.forward(200) #200 Denoting the size of the star
    star.right(144) #144 Denoting the Angle
    
turtle.done()