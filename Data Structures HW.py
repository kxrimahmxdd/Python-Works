average_speed = int(input("Enter your average speed in mph: "))
speed_limit = int(input("Enter the speed limit in mph: "))
distance = int(input("Enter the distance traveled in miles: "))

average_speed_time = distance / average_speed
time_at_speed_limit = distance / speed_limit

time_saved = time_at_speed_limit - average_speed_time
time_saved_minutes = time_saved * 60

# Corrected print statement with proper concatenation
print("You saved", int(time_saved_minutes), "minutes.")