from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.high_score()
        self.show_score()

    def show_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}, High Score: {self.high}', align='center', font=('Verdana', 15, 'normal'))

    def reset(self):
        if self.score>self.high:
            self.high = self.score
        self.score = -1
        self.high_score()
        self.show_score()

    def high_score(self):
        with open("high.txt", mode="r") as file:
            high = int(file.read())
        if self.high > high:
            with open("high.txt", mode="w") as file:
                file.write(str(self.high))
        else:
            self.high = high
