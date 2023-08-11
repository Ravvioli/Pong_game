import random
from turtle import Turtle

rand_int = [x for x in range(360)]
rand_int[80:100] = []
rand_int[230:250] = []
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def to_center(self):
        self.goto(0,0)
        self.setheading(random.choice(rand_int))


