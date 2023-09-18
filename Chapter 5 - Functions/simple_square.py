'''
'''

# Use turtle graphics
import turtle

# global constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
SQUARE_SIDE = 100
RIGHT_ANGLE = 90

# Draw a square
def draw_square():
    for x in range(4):
        turtle.forward(SQUARE_SIDE)
        turtle.right(RIGHT_ANGLE)

#  Position turtle at location
def position_turtle(xcoord, ycoord):
    turtle.penup()
    turtle.goto(xcoord, ycoord)
    turtle.pendown()     
# main
def main():
    # Position turtle -- pass by postion
    position_turtle(100, 100)
    # Draw square -- pass by keyword
    draw_square(length = 100, color = "blue")
    

# Start program by calling main
main()
turtle.done()