import turtle


def draw_squares(animal, size):
    for _ in range(4):
        for _ in range(4):
            animal.forward(40)
            animal.left(90)
        animal.forward(40)
        animal.penup()
        animal.forward(40)
        animal.pendown()


paper = turtle.Screen()
paper.bgcolor("pink")

square = turtle.Turtle()
square.color("blue")
draw_squares(square, 20)

paper.exitonclick()


