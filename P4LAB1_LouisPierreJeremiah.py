# Jeremiah Louis-Pierre
# 03/27/2024
# P4LAB1
# This program creates a square and a triangle using Turtle Graphics
import turtle

turtle.shape("arrow")

# Square
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

# Used to separate the shapes
turtle.forward(100)
turtle.left(120)

# Triangle
for i in range(3):
    turtle.forward(50)
    turtle.left(120)
turtle.exitonclick()
