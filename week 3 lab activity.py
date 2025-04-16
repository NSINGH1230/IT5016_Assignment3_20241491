
# Task 1: Python List Operations

# 1. Create a list of numbers from 1 to 10
numbers = list(range(1, 11))  # This creates the list [1, 2, ..., 10]

# 2. Print all elements of the list using a for loop
print("Task 1: List Elements:")
for num in numbers:
    print(num)

# 3. Append numbers (input from user)
for i in range(3):
    new_num = int(input(f"Enter a number to append (#{i + 1}): "))
    numbers.append(new_num)

# 4. Remove a number from the list (user input)
remove_num = int(input("Enter a number to remove from the list: "))
if remove_num in numbers:
    numbers.remove(remove_num)
else:
    print(f"{remove_num} is not in the list.")

# 5. Print final list
print("Final list:", numbers)


# Task 2: Python Dictionary Operations

# 1. Create a dictionary using user input
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
student_info = {
    'name': name,
    'age': age,
    'city': city
}
print("Student Info:", student_info)

# 2. Add email
email = input("Enter email: ")
student_info['email'] = email
print("Updated Info with Email:", student_info)

# 3. Update age
new_age = int(input("Enter new age: "))
student_info['age'] = new_age
print("Updated Info with New Age:", student_info)


# Task 3: While Loop

print("Task 3: While Loop - Print numbers from 1 to 10, stop at 7")
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1


# Task 4: For Loop

# Get student names from user
student_list = input("Enter student names separated by commas: ").split(',')

print("Greetings:")
for student in student_list:
    print("Hello,", student.strip() + "!")


# Task 5: Conditional Logic with if Statement

# Get grades from user
grades_input = input("Enter student grades separated by commas: ")
grades = [int(grade.strip()) for grade in grades_input.split(',')]

print("Pass or Fail:")
for grade in grades:
    if grade >= 80:
        print("Pass")
    else:
        print("Fail")


# Task 6: Combining All Concepts

print("\n--- Task 6: Combining All Tasks ---")

# List of numbers
combined_numbers = list(range(1, 11))

# Student dictionary using input
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_grade = int(input("Enter student grade: "))

student_data = {
    'name': student_name,
    'age': student_age,
    'grade': student_grade
}

# Print numbers using while loop
print("Numbers using while loop:")
i = 0
while i < len(combined_numbers):
    print(combined_numbers[i])
    i += 1

# Print student details
print("Student Details:")
for key, value in student_data.items():
    print(f"{key.capitalize()}: {value}")

# Check grade
if student_data['grade'] >= 80:
    print("Pass")
else:
    print("Fail")
