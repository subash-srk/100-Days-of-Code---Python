from turtle import Turtle, Screen
import random
tim = Turtle()
colours = ["Yellow", "Lime", "DarkGreen", "LightSkyBlue", "RoyalBlue", "LightSeaGreen", "Red", "DarkOrange"]
direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())