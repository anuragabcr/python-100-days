from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color(color)
        self.goto(x=x, y=0)
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
