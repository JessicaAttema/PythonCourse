class TravelMode:
    def __init__(self, mode, speed):
        self.mode = mode
        self.speed = speed

transport = [TravelMode("walking", 5), TravelMode("bike", 15), TravelMode("car", 50)]

ask_distance = int(input("What is the distance to uni? (in km) "))

for x in transport:
    print("The time to uni by", x.mode, "is ", x.speed * ask_distance)