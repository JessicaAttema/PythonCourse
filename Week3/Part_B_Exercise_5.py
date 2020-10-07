import turtle

paper = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape( "turtle")
size = 20

for _ in range (6):
    turtle.forward(50)
    turtle.left(60)

paper.exitonclick()
