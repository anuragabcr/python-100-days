import time
from turtle import Turtle, Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player
player = Player()
screen.onkey(fun=player.move, key='Up')
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    # Increase level
    if player.ycor() > 280:
        car.reset_game()
        player.reset_game()
        score.increase_score()

    # detect collision with cars
    for mack in car.turtles:
        if player.distance(mack) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
