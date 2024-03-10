import random
import time
from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(random.randrange(-45, 45))
        self.goto(0, 0)
        self.size = self.shapesize()[0]
        self.default_speed = 0.75
        self.speed = self.default_speed


    def move(self):
        self.forward(self.speed)

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280 :
            self.setheading(-self.heading())

    def rudder_collision(self, factor):
        self.speed = factor * self.default_speed
        self.setheading(180 - self.heading() - (factor-1) * 5)

    def restart(self, player):
        self.speed = self.default_speed
        self.goto(0, 0)
        if player == 1:
            self.setheading(random.randrange(135, 225))

        if player == 2:
            time.sleep(1)
            self.setheading(random.randrange(-45, 45))
