from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.penup()
        self.shape('circle')
        self.color('green')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(x=self.xcor()+self.x_move, y=self.ycor()+self.y_move)

    def collision_y(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.collision_x()
        self.move_speed = 0.1
