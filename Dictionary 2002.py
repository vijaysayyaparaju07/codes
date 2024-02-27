# An Empty dictionary
# 1. Create a dictionary to store session notes for student
Session_Notes = {} 

# A dictionary with multiple fields for the first student
# 2. Add session notes for Student
Student1 = {"Name": "Nithin", "Session Date": "2024-02-16", "Topic": "Arguments in Python",
            "Notes": "Default, Keyword, Variable length, Global,Local Variables"}
Session_Notes[Student1["Name"]] = Student1
# add the key-value pair to the dictionary using the name as the key

# 3. Add session notes for Student2
Student2 = {"Name": "Shiva", "Session Date": "2024-02-09", "Topic": "Data Structures in Python",
            "Notes": "Learned about lists, tuples, and dictionaries"}
# a dictionary with multiple fields for the second student
Session_Notes[Student2["Name"]] = Student2
# Add the key-value pair to the dictionary using the name as the key

# Print the dictionary
# 4. Add the notes to the session notes dictionary
print(Session_Notes)
#

# Ask the user to enter the name of the student
# 5. Accessing session notes for a specific student
Student_Name = input("Enter the name of the Student: ") 

if Student_Name in Session_Notes:   # Check if the name is in the dictionary
    print(Session_Notes[Student_Name])    # print the session notes for that student
else:    # if the name is not in the dictionary
    print("No Session Notes found for", Student_Name)    # print a message
