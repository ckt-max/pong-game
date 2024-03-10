from turtle import Turtle
import time
from scoreboard import Scoreboard


class Rudder(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.left(90)
        self.length = 5
        self.shapesize(0.5, self.length)
        # self.color('white')
        self.penup()
        self.score = Scoreboard()

    def up(self):
        if self.ycor() < 300 - self.length * 15:
            self.forward(2)

    def down(self):
        if self.ycor() > -300 + self.length * 15:
            self.back(2)
