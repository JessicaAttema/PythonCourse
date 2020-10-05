import turtle


def draw_spiral(animal, size):
    for _ in range(100):
        animal.right(91)
        size = size + 3
        animal.forward(size)


paper = turtle.Screen()
paper.bgcolor("pink")

spiral = turtle.Turtle()
spiral.color("blue")
draw_spiral(spiral, 3)

paper.exitonclick()
