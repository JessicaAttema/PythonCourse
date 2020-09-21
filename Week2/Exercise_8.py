ask_user = int(input("What time is it? "))

ask_wait = int(input("How many hours do you want to wait?: "))

final_time = (ask_user + ask_wait) % 24

set_alarm = print("The alarm will be set at: ", final_time)

