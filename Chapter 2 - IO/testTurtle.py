import turtle

turtle.title("Testing turtle graphics")
turtle.setup(400, 200, 500, 0)
turtle.speed(1)
turtle.bgcolor("pale green")
turtle.goto(0, -50)
turtle.setheading(90)
turtle.hideturtle()

turtle.begin_fill()
turtle.fillcolor("red")
turtle.forward(50)
turtle.right(45)
turtle.backward(50)
turtle.left(90)
turtle.end_fill()
turtle.penup()

turtle.forward(100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("light yellow")
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.down()
turtle.forward(50)
turtle.pendown()
turtle.write("Hello peeps!")

turtle.done()