from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align='center', font=('Verdana', 15, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.color('red')
        self.write(arg=f'Game Over', align='center', font=('Verdana', 20, 'normal'))
