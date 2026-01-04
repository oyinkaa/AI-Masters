# The dictionary for course number and the rooms they are held in
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# The dictionary for course number and the instructors that teach them
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary for the course schedule including course number and meeting times
course_schedule = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Ask the user for a course number
course_number = input("Enter a course number: ").upper()

# Display course information if it exists
if course_number in course_rooms:
    print("\nCourse Information:")
    print("Room Number:", course_rooms[course_number])
    print("Instructor:", course_instructors[course_number])
    print("Meeting Time:", course_schedule[course_number])
else:
    print("Invalid course number.")
