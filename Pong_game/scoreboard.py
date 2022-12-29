from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.player = color
        self.penup()
        self.color('white')
        self.goto(x, y)
        self.hideturtle()
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.player}: {self.score}", align='center', font=('Verdana', 15, 'normal'))
