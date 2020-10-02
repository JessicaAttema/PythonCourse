import turtle


def draw_pretty(animal, size):
    for _ in range(24):
        for _ in range(4):
            animal.forward(50)
            animal.left(90)
        animal.left(75)


paper = turtle.Screen()
paper.bgcolor("pink")

pretty = turtle.Turtle()
pretty.color("blue")
draw_pretty(pretty, 50)

paper.exitonclick()
