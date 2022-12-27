from turtle import Turtle, Screen

mack = Turtle()
screen = Screen()


def up():
    # mack.setheading(90)
    mack.forward(20)


def down():
    # mack.setheading(270)
    mack.backward(20)


def left():
    mack.setheading(mack.heading()-10)
    mack.forward(20)


def right():
    mack.setheading(mack.heading()+10)
    mack.forward(20)


def clear():
    mack.clear()
    mack.penup()
    mack.home()
    mack.pendown()


screen.listen()
screen.onkey(fun=up, key='Up')
screen.onkey(fun=down, key='Down')
screen.onkey(fun=left, key='Left')
screen.onkey(fun=right, key='Right')
screen.onkey(fun=clear, key='c')

screen.exitonclick()
