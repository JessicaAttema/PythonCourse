import turtle


def draw_poly(t, n, size):
    size = 50
    for _ in range(n):
        t.forward(20)
        t.left(45)


paper = turtle.Screen()
paper.bgcolor("pink")

tess = turtle.Turtle()
tess.color("blue")
draw_poly(tess, 8, 50)

paper.exitonclick()
