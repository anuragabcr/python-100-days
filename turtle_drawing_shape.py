import turtle
from turtle import Turtle
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
myTurtle = Turtle()
for i in range(3, 11):
    for _ in range(0, i):
        myTurtle.color(random.choice(colours))
        myTurtle.forward(100)
        myTurtle.left(360//i)

turtle.exitonclick()
