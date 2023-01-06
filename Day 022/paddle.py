from turtle import Turtle

VELOCITY = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() > 235:
            return
        self.goto(self.xcor(), self.ycor() + VELOCITY)

    def go_down(self):
        if self.ycor() < -235:
            return
        self.goto(self.xcor(), self.ycor() - VELOCITY)
