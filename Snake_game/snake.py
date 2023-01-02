from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape='square')
            snake.penup()
            snake.setposition(y=0, x=0 + (i * -20))
            snake.color('green')
            self.snakes.append(snake)

    def extend_snake(self):
        snake = Turtle(shape='square')
        snake.penup()
        snake.setposition(self.snakes[-1].pos())
        snake.color('green')
        self.snakes.append(snake)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].setposition(self.snakes[i - 1].pos())
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)
