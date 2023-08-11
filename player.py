from turtle import Turtle


class Player(Turtle):
    def __init__(self, number_):
        super().__init__()
        self.hideturtle()
        self.platform = []
        self.create_platform(number_)

    def create_platform(self, player_number):
        if player_number == 1:
            x = -285
        else:
            x = 278

        for i in range(4):
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(x, 20 - i*20)
            self.platform.append(turtle)

    def move_UP(self):
        if self.platform[0].ycor()<280:
            for i in self.platform:
                i.setheading(90)
                i.forward(45)

    def move_DOWN(self):
        if self.platform[-1].ycor()>-280:
            for i in self.platform:
                i.setheading(270)
                i.forward(45)

