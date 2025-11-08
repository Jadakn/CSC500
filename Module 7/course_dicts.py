course_to_room_number_dict = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_to_instructors_dict = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_to_times_dict = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

exit = False
while not exit:
    while True:
        try:
            course = input("Enter a course number (ex: CSC101), or 'exit' to quit: ")
            if course == 'exit':
                exit = True
                break
            if course not in course_to_room_number_dict:
                print("Course not found. Please enter a valid course number.")
                continue
            break
        except ValueError:
            print("Error: Input should be a valid course number.")
            continue

    if course in course_to_room_number_dict:
        print(f"Course Number: {course}")
        print(f"    Room Number: {course_to_room_number_dict[course]}")
        print(f"    Instructor: {course_to_instructors_dict[course]}")
        print(f"    Meeting Time: {course_to_times_dict[course]}")
    else:
        print("Course not found.")
