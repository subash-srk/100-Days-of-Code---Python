from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
for _ in range(15):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
