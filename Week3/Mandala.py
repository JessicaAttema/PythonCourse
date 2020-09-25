import turtle

paper = turtle.Screen()
mandala = turtle.Turtle()
mandala.shape("circle")
size = 20
mandala.speed(10)

for _ in range(36):
    mandala.color("pink")
    mandala.forward(200)
    mandala.left(170)

for x in range(36):
    mandala.color("red")
    mandala.backward(20)
    mandala.forward(240)
    mandala.left(170)


paper.exitonclick()

#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
    #forward(200)
    #left(170)
    #if abs(pos()) < 1:
        #break
#end_fill()
#done()