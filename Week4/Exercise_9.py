import turtle


def draw_star(animal, size):
    for _ in range(5):
        animal.forward(100)
        animal.right(144)



paper = turtle.Screen()
paper.bgcolor("pink")

star = turtle.Turtle()
star.color("blue")
draw_star(star, 2)

paper.exitonclick()