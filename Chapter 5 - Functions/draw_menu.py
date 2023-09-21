'''
    draw_menu.py
    Python programming example to use the simple_graphics.py module
    by displaying a menu of option and drawing the appropriate graphic.
    '''
    
import simple_graphics as sg
import turtle
import random

# Named constants for menu choices
SQUARE = 1
TRIANGLE = 2
CIRCLE = 3
ROMBUS = 4
PENTAGON = 5
HEXAGON = 6

def display_menu():
    print("Draw Menu")
    print("---------")
    print("1. Draw square")
    print("2. Draw right triangle")
    print("3. Draw circle") 
    print("4. Draw rombus")
    print("5. Draw pentagon")
    print("6. Draw hexagon")
    print("7. Quit")   
    print()

def main():
    # Get user menu selection
    display_menu()
    choice = int(input("Enter your menu choice: "))
     
    #setup window and turtle
    turtle.setup(600, 600, 2000, 5)
    turtle.title("Drawing Menu")

 
    # Get random coordinates
    x_pos = random.randint(-200, 200)
    y_pos = random.randint(-200, 200)
    sg.postion_turtle(x_pos, y_pos) # To position the turtle
 
    #Determine the shape to draw
    if choice == SQUARE:
        side = float(input("Enter the square side (in pixels): "))
        sg.draw_square(random.choice(sg.COLORS), side)
    elif choice == TRIANGLE:
        side = float(input("Enter the triangle side (in pixels): "))
        sg.draw_right_triangle(random.choice(sg.COLORS), side)
    elif choice == CIRCLE:
        radius = float(input("Enter the circle radius (in pixels): "))
        sg.draw_circle(random.choice(sg.COLORS), radius)
    elif choice == ROMBUS:
        side = float(input("Enter the rombus side (in pixels): "))
        angle = float(input("Enter the rombus angle (Between 90 and 180 degrees): "))
        while angle < 90 or angle > 180:
            angle = float(input("Enter the rombus angle (Between 90 and 180 degrees): "))
        sg.draw_rombus(random.choice(sg.COLORS), side, angle)
    elif choice == PENTAGON:
        side = float(input("Enter the pentagon side (in pixels): "))
        sg.draw_pentagon(random.choice(sg.COLORS), side)
    elif choice == HEXAGON:
        side = float(input("Enter the hexagon side (in pixels): "))
        sg.draw_hexagon(random.choice(sg.COLORS), side)
    elif choice == 7:
        print("Exiting the program...")
        exit()
    else:
        print("Error! Invalid menu selection.")
        exit()
    turtle.hideturtle()
    turtle.done()
   
# Call the main function
main()
