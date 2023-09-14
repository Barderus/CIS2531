'''
Author: Gabriel dos Reis
Date: 9/12/2023
Program: spiralCircles
Description: Use turtle to create a spiral circle
'''

import turtle

#Named Constants
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0.9

# Set the animation speed
turtle.speed(ANIMATION_SPEED)

#Draw 36 circles, with the turtle tilted
#By 10 degrees after each circle is drawn
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()