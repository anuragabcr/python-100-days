import turtle
from turtle import Turtle, Screen
import pandas as pd

df = pd.read_csv(r"states.csv")

screen = Screen()
screen.setup(width=600, height=700)
screen.title("India State Game")
screen.addshape("India-locator-map-blank.gif")
turtle.shape("India-locator-map-blank.gif")

mack = Turtle()
mack.penup()
mack.hideturtle()

guessed = []

while len(guessed) < 38:
    name = screen.textinput(title=f'{len(guessed)}/38 States', prompt="Enter one of the india's state name: ").capitalize()

    if name == 'Exit':
        learn = df[~df['State'].isin(guessed)]
        learn.to_csv('Learn.csv')
        break

    cor = df[df['State'] == name]
    if len(cor):
        mack.goto(x=int(cor['X']), y=int(cor['Y']))
        mack.write(arg=name, font=('Verdana', 10, 'normal'))
        guessed.append(name)

# turtle.mainloop()

# bellow fn is used to get the state coordinate from the image
# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)
# screen.exitonclick()

