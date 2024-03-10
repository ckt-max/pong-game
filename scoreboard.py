from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.color('gray')
        self.score = 0
        # self.goto(0, 250)

    def show(self):
        self.write(self.score, move=False, align='center', font=('Broadway', 30, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, align='center', font=('Broadway', 30, 'normal'))

    def over(self, name):
        self.goto(0, 0)
        self.write(f'{name} is the winner', move=False, align='center', font=('Broadway', 30, 'normal'))

