import time

from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard

# setting up the screen
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=500)
screen.bgcolor('black')
screen.tracer(0)
middle_line = Turtle(shape='square')
middle_line.color('white')
middle_line.penup()
middle_line.shapesize(stretch_wid=1, stretch_len=25)
middle_line.setheading(90)
screen.listen()

# create player and ball
ball = Ball()
paddle1 = Paddle(x=-380, color='dark turquoise')
paddle2 = Paddle(x=370, color='cornflower blue')
score1 = Scoreboard(x=-120, y=220, color='dark turquoise')
score2 = Scoreboard(x=120, y=220, color='cornflower blue')

# calling the listener
screen.onkey(fun=paddle2.up, key='Up')
screen.onkey(fun=paddle2.down, key='Down')
screen.onkey(fun=paddle1.up, key='w')
screen.onkey(fun=paddle1.down, key='s')

# running the game
while True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.collision_y()

    # detect collision with paddle
    if ball.distance(paddle1) < 40 or ball.distance(paddle2) < 40:
        ball.collision_x()

    # detect ball miss
    if ball.xcor() > 380:
        ball.reset_position()
        score1.increase_score()
    if ball.xcor() < -370:
        ball.reset_position()
        score2.increase_score()

screen.exitonclick()
