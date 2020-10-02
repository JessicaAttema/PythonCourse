import turtle


def draw_spiral(animal, size):
    for _ in range(15):
        for _ in range(4):
            animal.right(90)
            size = size + 2
            animal.forward(size)
        animal.left(5)


paper = turtle.Screen()
paper.bgcolor("pink")

spiral = turtle.Turtle()
spiral.color("blue")
draw_spiral(spiral, 2)

paper.exitonclick()
