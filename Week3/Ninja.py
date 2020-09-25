import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.shape( "turtle")
size = 20

for _ in range(30):
    leonardo.forward(25)
    leonardo.left(30)
    size = size + 2
    leonardo.forward(size)



paper.exitonclick()

