import time
from turtle import Screen
from ball import Ball
from player import Player
from scoreboard import Scoreboard
import random


def main():
    # TODO: fix resolution settings
    # TODO: fix game_over txt
    RESOLUTION_W = 600
    RESOLUTION_H = 600

    screen = Screen()
    screen.setup(RESOLUTION_W, RESOLUTION_H)
    screen.bgcolor("black")
    screen.tracer(0)

    scoreboard_1 = Scoreboard()
    scoreboard_1.goto(-100, 250)
    scoreboard_1.refresh()
    scoreboard_2 = Scoreboard()
    scoreboard_2.goto(100, 250)
    scoreboard_2.refresh()

    scoreboard_1.make_line()
    # ----------------------------------------
    ball = Ball()
    rand_int = [x for x in range(360)]
    rand_int[80:100] = []
    rand_int[230:250] = []
    ball.setheading(random.choice(rand_int))
    # ----------------------------------------
    player_1 = Player(1)
    player_2 = Player(2)
    # ---------------------------------------
    screen.listen()
    screen.onkey(player_1.move_UP,"w")
    screen.onkey(player_1.move_DOWN,"s")
    screen.onkey(player_2.move_UP,"Up")
    screen.onkey(player_2.move_DOWN,"Down")
    # ----------------------------------------
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        ball.forward(20)

        if ball.ycor()>290:
            ball.setheading(-ball.heading())
        elif ball.ycor()< -290:
            ball.setheading(-ball.heading())
        if ball.xcor() < -300:
            scoreboard_2.score += 1
            ball.to_center()
            scoreboard_2.refresh()

        if ball.xcor() > 300:
            scoreboard_1.score += 1
            ball.to_center()
            scoreboard_1.refresh()
        for i in range(4):
            if ball.distance(player_1.platform[i]) < 20 or ball.distance(player_2.platform[i]) < 20:
                ball.setheading(-ball.heading() + 180)
                ball.forward(20)
                continue
        if scoreboard_1.score >10 or scoreboard_2.score >10:
            game_is_on = False


    screen.exitonclick()


if __name__ == "__main__":
    main()
