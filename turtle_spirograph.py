import turtle
import random

turtle.colormode(255)
myTurtle = turtle.Turtle()
myTurtle.speed(50)
for i in range(0, 360, 5):
    myTurtle.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    myTurtle.circle(100)
    myTurtle.setheading(i)

turtle.exitonclick()