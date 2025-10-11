try:
    present_time = int(input("Enter what time it is currently (0-23): "))
    if present_time < 0 or present_time > 23:
        raise ValueError("The current time must be an integer between the values 0 and 23.")
    hours_until_alarm = int(input("Enter how many hours you want to wait for the alarm: "))
    if hours_until_alarm < 0:
        raise ValueError("Alarm hours must be a non-negative integer.")
except ValueError as err:
    if "invalid literal for int()" in str(err):
        print("Error: Please enter a numeric integer value.")
    else:
        print(f"Error: {err}")
    exit()
time_for_alarm = (present_time + hours_until_alarm) % 24
print("The alarm will go off at the following time: " + str(time_for_alarm) + ":00")
