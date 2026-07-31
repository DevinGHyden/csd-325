# Name: Devin G. Hyden
# Date: 31 July 2026
# Assignment: Module 8.2 Assignment

import json

# Loops through and formats outputs
def print_student_list(students):
    # Iterates over each dictionary entry in the list
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load the JSON file into Python list using load()
filename = 'Student.json'

with open(filename, 'r') as file:
    student_list = json.load(file)

# Output notification for original list
print("--- Original Student List ---")

# Call print function
print_student_list(student_list)

# Create a new student dictionary and append to the list
new_student = {
    "F_Name": "Devin",
    "L_Name": "Hyden",
    "Student_ID": 41100,
    "Email": "dhyden@my365.bellevue.edu"
}

student_list.append(new_student)

# Output notification for updated list
print("\n--- Updated Student List ---")

# Call print function
print_student_list(student_list)

# Save the updated list back to the JSON file
with open(filename, 'w') as file:
    json.dump(student_list, file, indent=4)

# Output notification that JSON file was updated
print("\nNotification: The student.json file has been updated successfully")