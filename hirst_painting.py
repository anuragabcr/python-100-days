import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract("hirst-art.jpg",25)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

turtle.colormode(255)
myTurtle = turtle.Turtle()

for i in range(10):
    myTurtle.penup()
    myTurtle.goto(-250.0, -250+(i*50))
    for j in range(10):
        myTurtle.pendown()
        myTurtle.color(random.choice(rgb_colors))
        myTurtle.dot(20)
        myTurtle.penup()
        myTurtle.forward(50)

turtle.exitonclick()