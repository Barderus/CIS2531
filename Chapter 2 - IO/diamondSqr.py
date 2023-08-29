'''
Author: Gabriel dos Reis
Class: CIS2531 - Intro to Python
Date: 8/28/2023
Prog: diamondSqr.py
Description: Create a drawing of a diamond with the colors blue, black, green, and red.
Under the design, add the following statement: "A colorful diamond square by Gabriel dos Reis"
'''

import turtle

#named constants
CENTER_X = 0
CENTER_Y = 0

#Set window characteristics
turtle.setup(500, 500, 500, 0)
turtle.title("Diamond Square")

#Hide turtle and set animation speed
turtle.hideturtle()
turtle.speed(1)

#Make diamond 1 ( Green)
turtle.goto(CENTER_X, CENTER_Y)
turtle.begin_fill()
turtle.fillcolor("green")
turtle.goto(-50, -75)
turtle.goto( 0,-150)
turtle.goto(50, -75)
turtle.goto(CENTER_X, CENTER_Y)
turtle.end_fill()

#Make diamond 2 (Black)
turtle.begin_fill()
turtle.fillcolor("black")
turtle.goto(50, -75)
turtle.goto(110, CENTER_Y)
turtle.goto(50, 75)
turtle.goto(CENTER_X, CENTER_Y)
turtle.end_fill()

# Make diamond 3 (Red)
turtle.begin_fill()
turtle.fillcolor("red")
turtle.goto(-50, 75)
turtle.goto(-110, CENTER_Y)
turtle.goto(-50, -75)
turtle.end_fill()

#Make diamond 4 (Blue)
turtle.penup()
turtle.goto(-50, 75)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.goto(0, 150)
turtle.goto(50,75)
turtle.goto(CENTER_X, CENTER_Y)
turtle.end_fill()

#Write statement under the diamond
turtle.penup()
turtle.goto(-85, -165)
turtle.pendown()
turtle.write("Diamond Square by Gabriel dos Reis")

#Keep the window open
turtle.done()
