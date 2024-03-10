from turtle import Screen, Turtle
import time
from random import *
from rudder import Rudder
from ball import Ball

# State machine to track which keys are pressed:
keys_pressed = {}
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('#52c234')
screen.title('PONG')

# line that separates the player's fields
mid_line = Turtle()
mid_line.hideturtle()
mid_line.pensize(10)
mid_line.color('yellow')
mid_line.penup()
mid_line.goto(0, 300)
mid_line.pendown()
mid_line.goto(0, -300)
is_game_on = True
screen.tracer(0)

player1 = Rudder()
player1.goto(-350, 0)


player2 = Rudder()
player2.goto(350, 0)

ball = Ball()

# initializing scoreboards:
player1.score.goto(-50, 250)
player1.score.show()
player2.score.goto(+50, 250)
player2.score.show()


# Callback for KeyPress event listener. Sets key pressed state to True
def pressed(event):
    keys_pressed[event.keysym] = True

# Callback for KeyRelease event listener. Sets key pressed state to False
def released(event):
    keys_pressed[event.keysym] = False

# Set up the event listeners, bypassing the Turtle Screen to use the underlying TKinter canvas directly
# This needs to be done to get access to the event object so the state machine can determine which key was pressed
def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


screen.listen()
set_key_binds()

while is_game_on:

    #time.sleep(0.1)
    ball.move()
    ball.wall_collision()

    # Detecting rudder collision with the ball:
    if ball.xcor() <= player1.xcor()+10 and ball.xcor() > player1.xcor()-10 and ball.distance(player1) < 60:
        factor = ball.distance(player1)/20 + 1
        ball.rudder_collision(factor)


    if ball.xcor() >= player2.xcor()-10 and ball.xcor() < player2.xcor()+10 and ball.distance(player2) < 60:
        factor = ball.distance(player2)/33 + 1
        ball.rudder_collision(factor)

    if keys_pressed["w"]:
        player1.up()
    if keys_pressed["s"]:
        player1.down()
    if keys_pressed["Up"]:
        player2.up()
    if keys_pressed["Down"]:
        player2.down()

    # Detecting if the ball has gone out and updating score:
    if ball.xcor() > 420:
        player1.score.update()
        ball.restart(1)

    if ball.xcor() < -420:
        player2.score.update()
        ball.restart(2)

    # End of Game
    if player1.score.score == 10:
        ball.hideturtle()
        time.sleep(1)
        player1.score.over('Player 1')
        is_game_on = False

    elif player2.score.score == 10:
        time.sleep(1)
        ball.hideturtle()
        player1.score.over('Player 2')
        is_game_on = False

    screen.update()


screen.exitonclick()
