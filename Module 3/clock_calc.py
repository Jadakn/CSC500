try:
    current_time = int(input("Enter the current time (0-23): "))
    if current_time < 0 or current_time > 23:
        raise ValueError("Time must be between 0 and 23.")
    alarm_hours = int(input("Enter the number of hours to wait for the alarm: "))
    if alarm_hours < 0:
        raise ValueError("Alarm hours must be a non-negative integer.")
except ValueError as e:
    if "invalid literal for int() with base 10: " in str(e):
        print("Error: Please enter a numeric integer value.")
    else:
        print(f"Error: {e}")
    exit()
alarm_time = (current_time + alarm_hours) % 24
print(f"The alarm will go off at {alarm_time}:00.")
