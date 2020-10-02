import turtle


def draw_squares_again(animal, size):
    for _ in range(8):
        size = size + 20
        for _ in range(4):
            animal.forward(size)
            animal.left(90)
        animal.setheading(225)
        animal.penup()
        animal.forward(14)
        animal.pendown()
        animal.setheading(0)


paper = turtle.Screen()
paper.bgcolor("pink")

squares = turtle.Turtle()
squares.color("blue")
draw_squares_again(squares, 5)

paper.exitonclick()
