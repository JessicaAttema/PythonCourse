import turtle

paper = turtle.Screen()
star = turtle.Turtle()
star.shape("turtle")

for x in range(5):
    star.forward(100)
    star.right(144)
    star.forward(100)

paper.exitonclick()
