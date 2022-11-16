from turtle import Turtle,Screen
import random
t=Turtle()
t.pensize(15)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[0,90,180,270]
t.speed(9)
for i in range(200):
    t.forward(30)
    t.setheading(random.choice(direction))

    t.color(random.choice(colours))




screen=Screen()
screen.exitonclick()


