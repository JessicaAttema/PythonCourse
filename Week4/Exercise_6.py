import turtle


def draw_triangle(t, size):
    draw_poly(t, n, size)


paper = turtle.Screen()
paper.bgcolor("pink")

triangle = turtle.Turtle()
triangle.color("blue")
draw_triangle(triangle, 100)

paper.exitonclick()
