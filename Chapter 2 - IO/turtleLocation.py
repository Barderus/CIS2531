import turtle

#Set window characteristics
turtle.setup(600, 600, 2000, 5)
turtle.title("My house")
turtle.bgcolor("Sky blue")

#Hide turtle and set animation speed
turtle.hideturtle()
turtle.speed(1)

# self defined function to print coordinate
def buttonclick(x,y):
	print("You clicked at this coordinate({0},{1})".format(x,y))

#onscreen function to send coordinate
turtle.onscreenclick(buttonclick,1)
turtle.listen() # listen to incoming connections
turtle.speed(10) # set the speed

turtle.done()