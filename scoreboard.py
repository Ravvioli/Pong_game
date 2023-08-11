from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.refresh()
        print(__name__)

    def refresh(self):
        self.clear()
        self.write(f"{self.score}", font=("Arial", 30, "normal"))

    def add_point(self):
        self.score +=1
        self.refresh()

    def make_line(self):
        line = Turtle()
        line.color("white")
        line.hideturtle()
        line.penup()
        line.goto(0,-280)
        line.setheading(90)
        while line.ycor() < 340:
            line.color("white")
            line.pendown()
            line.forward(25)
            line.penup()
            line.forward(30)
