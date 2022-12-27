import turtle
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [90, 180, 270, 360]
distances = [10, 15, 20, 25]
turtle.colormode(255)
myTurtle = turtle.Turtle()
myTurtle.speed(20)
myTurtle.pensize(10)
for i in range(0, 100):
    # myTurtle.color(random.choice(colours))
    myTurtle.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    myTurtle.forward(random.choice(distances))
    myTurtle.setheading(random.choice(angles))

turtle.exitonclick()