'''
Author: Gabriel dos Reis
Date: 9/12/2023
Program: colorfulCircle.py
Description: Use the turtle graphics library to create a Colorful Circles Python program
that uses nested loops to draw 3 rows of different colored circles in each row.  
Rows can have any number of circles in the range of 3 to 12.  
Prompt, read, and validate user input number of columns and colors.  
Create a colorful circles drawing when input is in the valid ranges.
'''

import turtle

# Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Hide turtle and set drawing speed
turtle.hideturtle()
turtle.speed(0)

# Prompt, read, and validate the number of columns (3 to 12)
columns = 0
while True:
    try:
        columns = int(input("Enter the number of columns (3 to 12): "))
        if 3 <= columns <= 12:
            break
        else:
            print("Please enter a valid number between 3 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompt, read, and validate three different colors
color1 = input("Enter the color for the first row: ")
color2 = input("Enter the color for the second row: ")
color3 = input("Enter the color for the third row: ")

while color1 == color2 or color1 == color3 or color2 == color3:
    print("Please make sure the colors are different for each row.")
    color1 = input("Enter the color for the first row: ")
    color2 = input("Enter the color for the second row: ")
    color3 = input("Enter the color for the third row: ")

# Calculate the radius of circles based on the number of columns
circle_radius = 50 / columns

# Loop through each row
for row in range(3):
    turtle.penup()
    # Calculate the starting x-coordinate for the row
    start_x = 0 - circle_radius / 2
    # Set the initial position of the turtle
    turtle.goto(start_x, 100 - row * 2 * circle_radius)

    # Assign the color for this row
    if row == 0:
        color = color1
    elif row == 1:
        color = color2
    else:
        color = color3

    # Loop through each column
    for column in range(columns):
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(circle_radius)
        turtle.end_fill()
        turtle.penup()
        # Move to the next column
        turtle.forward(2 * circle_radius)

# Close the turtle graphics window on click
turtle.done()
