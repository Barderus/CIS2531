'''
Draw the Chicago Sillhoette
'''
import turtle

#Set window characteristics
turtle.setup(1000, 1000, 2000, 0)
turtle.title("Chicago Sillhoette")
turtle.bgcolor("DarkBlue")

# Hide turtle and set animation speed
#turtle.hideturtle()
turtle.speed(1)

# self defined function to print coordinate
def buttonclick(x,y):
	print("You clicked at this coordinate({0},{1})".format(x,y))

#  onscreen function to send coordinate
turtle.onscreenclick(buttonclick,1)
turtle.listen() # listen to incoming connections
turtle.speed(1) # set the speed

# Draw the Chicago Sillhoette
turtle.goto(-300, 0)

turtle.done()

