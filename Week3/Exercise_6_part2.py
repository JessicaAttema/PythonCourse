
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle

paper = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape( "circle")
size = 20

for x in angles:
    turtle.forward(100)
    turtle.left(x)

paper.exitonclick()
