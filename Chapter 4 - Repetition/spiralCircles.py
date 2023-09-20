'''
Author: Gabriel dos Reis
Date: 9/12/2023
Program: spiralCircles
Description: Use turtle to create a spiral circle
'''

import turtle
import random

#Named Constants
NUM_CIRCLES = 36
RADIUS = 150
ANGLE = 10
ANIMATION_SPEED = 0.5

# Set the animation speed
turtle.speed(ANIMATION_SPEED)
turtle.bgcolor("black")

#Draw 36 circles, with the turtle tilted
#By 10 degrees after each circle is drawn
for x in range(NUM_CIRCLES):
    line_color = random.choice(["red", "green", "blue", "yellow", "orange", "purple"])
    turtle.color(line_color)
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
turtle.hideturtle()
turtle.done()