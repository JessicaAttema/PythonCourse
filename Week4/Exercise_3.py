import turtle


def draw_poly(t, n, size):
    for _ in range(n):
        t.forward(size)
        t.left(360/n)


paper = turtle.Screen()
paper.bgcolor("pink")

tess = turtle.Turtle()
tess.color("blue")
draw_poly(tess, 8, 50)

paper.exitonclick()

