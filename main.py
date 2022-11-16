import turtle
from turtle import Turtle,Screen
import random
t=Turtle()
t.pensize(15)
turtle.colormode(255)
direction=[0,90,180,270]
t.speed(9)
def color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r,g,b)
    return random_color
for i in range(200):
    t.forward(30)
    t.setheading(random.choice(direction))

    t.color(color())




screen=Screen()
screen.exitonclick()


