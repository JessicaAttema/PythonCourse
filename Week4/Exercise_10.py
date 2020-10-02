import turtle


def draw_stars(animal, size):
    for _ in range (5):
        for _ in range(5):
            animal.forward(100)
            animal.right(144)
        animal.penup()
        animal.forward(350)
        animal.right(144)
        animal.pendown()



paper = turtle.Screen()
paper.bgcolor("pink")

stars = turtle.Turtle()
stars.color("blue")
draw_stars(stars, 2)

paper.exitonclick()