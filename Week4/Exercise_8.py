def area_of_circle(r):
    a = r ** 2
    return a

radius = float(input("What is the radius?"))
area = area_of_circle(radius)
print("The area of the circle is: ", area)
