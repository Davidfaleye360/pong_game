from turtle import Turtle
WIDTH, HEIGHT = 20, 100


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')

    def move_up(self):
        y = self.ycor()
        if y < 250:
            self.sety(y+30)

    def move_down(self):
        y = self.ycor()
        if y > -250:
            self.sety(y-30)

