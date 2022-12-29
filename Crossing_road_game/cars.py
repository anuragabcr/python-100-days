import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = list(range(270, -270, -30))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.turtles = []
        self.create()
        self.new_create = 0

    def create(self):
        mack = Turtle(shape='square')
        mack.penup()
        mack.goto(x=280, y=random.choice(STARTING_POSITION))
        mack.color(random.choice(COLORS))
        mack.setheading(180)
        self.turtles.append(mack)

    def move(self):
        self.new_create += 1
        if self.new_create == 5:
            self.new_create = 0
            self.create()
        for mack in self.turtles:
            mack.forward(STARTING_MOVE_DISTANCE)

    def reset_game(self):
        # for mac in self.turtles:
        #    mac.reset()
        # self.turtles = []
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
