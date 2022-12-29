from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=250)
        self.score = 0
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align='center', font=FONT)
