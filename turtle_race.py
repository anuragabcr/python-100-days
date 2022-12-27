from turtle import Turtle, Screen
import random

screen = Screen()
turtles = []
colors = ['red', 'green', 'orange', 'blue', 'black']
speeds = [10, 11, 12, 13, 14, 15]

screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet: ", prompt=f"Enter a turtle color on which you want to bet?{colors}: ")
for i in range(5):
    tur = Turtle(shape='turtle')
    tur.color(colors[i])
    tur.penup()
    tur.goto(x=-230, y=-100+(50*i))
    turtles.append(tur)

while True:
    for i in range(5):
        turtles[i].forward(random.choice(speeds))
        if turtles[i].position()[0] > 250:
            if colors[i] == choice:
                print("You won the bet")
            else:
                print("You lose the bet")
            print(f"{colors[i]} won the race.")
            exit()
