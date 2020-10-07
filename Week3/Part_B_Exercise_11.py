import turtle

paper = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
size = 20

turtle.left(90)
for x in range(12):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(10)
    turtle.stamp()
    turtle.setx(0)
    turtle.sety(0)
    turtle.left(30)

paper.exitonclick()