'''
'''
import turtle
RIGHT_ANGLE = 90
EAST = 0

def draw_square(color, length):
    ''' Draw filled square.
    
    Parameters:
    color --> String fill color
    length --> side lenght in pixels
    
    Description:
    Draw color filled square with sides of equal length
    and all right angles at current location.
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(length)
        turtle.right(RIGHT_ANGLE)
    turtle.end_fill()
    
def postion_turtle(x_coord, y_coord):
    ''' Position turtle at given location
    
    Parameters:
    x_coord --> x coordinate in pixels
    y_coord --> y coordinate in pixels
    
    Description:
    Without drawing, position turtle facing EAST at gievn x_coord
    and y_coord.
    '''
    turtle.penup()
    turtle.goto(x_coord, y_coord)
    turtle.setheading(EAST)
    turtle.pendown()
    
def main():
    
    #setup window and turtle
    turtle.setup(600, 600, 2000, 5)
    turtle.title("Drawing Menu")
    
    turtle.goto(60)
    
    draw_square("black", 50)
    turtle.done()
    
main()
