from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position[0], position[1])
        self.suunta = 0

    def suunta_up(self):
        self.suunta = 1

    def suunta_empty(self):
        self.suunta = 0

    def suunta_down(self):
        self.suunta = -1

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)

    def move(self):
        if self.suunta == 1:
            self.go_up()
        elif self.suunta == -1:
            self.go_down()
