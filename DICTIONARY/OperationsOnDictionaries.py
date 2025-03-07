# Dictionaries

# 1.1 Creating a dictionary with 5 key-value pairs (Student ID and Name)
students = {
    1: "Hari",
    2: "Swetha",
    3: "Surya",
    4: "Radha",
    5: "Veera"
}
print("Dictionary:", students)

# 1.2 Updating a value in the dictionary
students[3] = "Krishna"  # Updating Charlie to Chris
print("\nAfter Updating Student ID 3:", students)

# 1.3 Accessing a value in the dictionary
print("\nAccessing Student ID 2:", students[2])

# 1.4 Creating a nested dictionary (Student ID with Subject-wise Marks)
students_data = {
    1: {"Name": "Hari", "Marks": {"Python": 90, "SQL": 85}},
    2: {"Name": "Swetha", "Marks": {"Python": 80, "SQL": 88}},
    3: {"Name": "Krishna", "Marks": {"Python": 95, "SQL": 92}},
}

# 1.5 Accessing values from the nested dictionary
print("\nMarks of Student ID 1 in Python:", students_data[1]["Marks"]["Python"])

# 1.6 Printing keys present in a dictionary
print("\nKeys in Students Dictionary:", students.keys())

# 1.7 Deleting a value from the dictionary
del students[4]  # Removing Student ID 104
print("\nAfter Deleting Student ID 4:", students)
