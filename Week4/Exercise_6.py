import turtle


def draw_poly(t, n, size):
    for _ in range(n):
        t.forward(size)
        t.left(360/n)


def draw_triangle(t, size):
    draw_poly(t, 3, size)


paper = turtle.Screen()
paper.bgcolor("pink")

triangle = turtle.Turtle()
triangle.color("blue")
draw_triangle(triangle, 100)

paper.exitonclick()
