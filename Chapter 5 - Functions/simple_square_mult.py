'''
Author:
Date:
Prorgram:
Description:
'''
import turtle
import random


# Global constants
ANIMATION_SPEED = 10
EAST = 0
RIGHT_ANGLE = 90
MIN_SIDE = 10
MAX_SIDE = 100
DELTA = 10
MIN_COORD = -200
MAX_COORD = 200

turtle.speed(ANIMATION_SPEED)
def get_rand_size(min_val, max_val, step_val):
    ''' return side length in the range of min_val, max_val, and step_val'''
    return random.randrange(min_val, max_val, step_val)

def get_rand_coord(min_x, min_y, max_x, max_y):
    ''' return random x and y coordinates in the range of min_x, min_y, max_x, and max_y'''
    x = random.randrange(min_x, max_x)
    y = random.randrange(min_y, max_y)
    return x, y

# Position turtle at location
def position_turtle(xcoord, ycoord):
    ''' Position turtle at given location '''
    turtle.penup()
    turtle.goto(xcoord, ycoord)
    turtle.setheading(EAST) # make sure turtle is facing East
    turtle.pendown() 
    
# Draw a square
def draw_square(color, length):
    ''' Draw a square of given color and size'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(length)
        turtle.right(RIGHT_ANGLE)
    turtle.end_fill()

def draw_rectangle(color, length):
    ''' Draw a rectangle of given color and size'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(length)
        turtle.right(RIGHT_ANGLE)
        turtle.forward(length * 2)
        turtle.right(RIGHT_ANGLE)
    turtle.end_fill()

def draw_triangle(color, length):
    ''' Draw a triangle of given color and size'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(length)
        turtle.right(120)
    turtle.end_fill()

def get_random_color():
    return random.choice(["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "gold", "silver", "cyan", "magenta", "violet", "indigo"])

def get_random_side():
    return get_rand_size(MIN_SIDE, MAX_SIDE, DELTA)

def main():
    # Get the number of shapes to draw
    num_shapes = int(input("Enter the number of shapes to draw: "))
    
    # Draw the given number of shapes
    for shape in range(num_shapes):
        fillcolor = get_random_color()
        shape_side = get_random_side()
        x_pos, y_pos = get_rand_coord(MIN_COORD, MIN_COORD, MAX_COORD, MAX_COORD)
        position_turtle(x_pos, y_pos)
        
        # Choose a random shape to draw
        random_shape = random.choice([draw_square, draw_rectangle, draw_triangle])
        random_shape(fillcolor, shape_side)

main()
turtle.hideturtle()
turtle.done()
