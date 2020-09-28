
# true and true = true
# true and false = false
# false and true and false and true and true = false
# true or false = true
# false or false = false
# false or false or true = true

start = int(input("What day number is today (between 0 and 6)"))

daagjes = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

length = int(input("How long is your stay?: "))

day_return = (length + start) % 7

print("You return on a: ", daagjes[day_return])



