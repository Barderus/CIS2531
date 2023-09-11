'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: targetGame.py
Description:
'''

import  turtle

# Named constants
SCREEN_WDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# Setup the window
turtle.setup(SCREEN_WDTH, SCREEN_HEIGHT)

# Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance
distance = force * FORCE_FACTOR

# Set the heading
turtle.setheading(angle)

# Launch the projectile
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?

# First check the x-coordinate to see if in range
inXrange = turtle.xcor() >= TARGET_LLEFT_X and \
           turtle.xcor() <= TARGET_LLEFT_X + TARGET_WIDTH
inYrange= turtle.ycor() >= TARGET_LLEFT_Y and \
          turtle.ycor() <= TARGET_LLEFT_Y + TARGET_WIDTH  
if inXrange and inYrange:
    print("Target hit!")
    turtle.write("TARGET HIT!")
else:
    print("You missed the target.")
turtle.done()

