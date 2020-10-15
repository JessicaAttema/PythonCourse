import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

for _ in range(5):
    tess.forward(20)

# tess is also pink, because tess is assigned to alex, so they both refer to the same object
