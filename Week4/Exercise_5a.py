import turtle


def draw_spiral(animal, size):
    for _ in range(50):
        animal.right(90)
        size = size + 5
        animal.forward(size)


paper = turtle.Screen()
paper.bgcolor("pink")

spiral = turtle.Turtle()
spiral.color("blue")
draw_spiral(spiral, 5)

paper.exitonclick()
