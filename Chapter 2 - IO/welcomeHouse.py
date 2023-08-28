'''
Author: Gabriel dos Reis
Class: CIS2531 - Intro to Python
Date: 8/28/2023
Prog: welcomeHouse.py
Description: Create a drawing of a house and a sun with a welcoming message
'''

from math import sqrt
import turtle #Make turtle methods visible available for this file

#named constants for direction
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
RIGHT_ANGLE = 90
RADIUS = 25
HOUSE_SIDE = 200
CENTER_X = 0
CENTER_Y = 0

#Set window characteristics
turtle.setup(500, 500, 500, 0)
turtle.title("My house")
turtle.bgcolor("Sky blue")

#Hide turtle and set animation speed
turtle.hideturtle()
turtle.speed(1)

#Draw the sun
turtle.penup()
#Turtle go to this position
turtle.goto(100, 100)
turtle.pendown()
#Turtle make a circle with 25 radius and fill it with color gold
turtle.begin_fill()
turtle.fillcolor("gold")
turtle.circle(RADIUS)
turtle.end_fill()

#Draw the house
#Start with the roof
turtle.penup()
turtle.goto(CENTER_X - HOUSE_SIDE, CENTER_Y)
turtle.setheading(RIGHT_ANGLE/2)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("orange red")
turtle.forward(HOUSE_SIDE/2)
turtle.right(RIGHT_ANGLE)
turtle.forward(HOUSE_SIDE/2)
turtle.setheading(WEST)

# Using pythagorean theorem to find the 3rd side
# a^2 + b^2 = c^2
roof = sqrt((HOUSE_SIDE/2) ** 2 + (HOUSE_SIDE/2) ** 2)
turtle.forward(roof)
turtle.end_fill()

# Continue with the house

#Keep the window open
turtle.done()

