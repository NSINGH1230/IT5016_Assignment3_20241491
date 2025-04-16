# Function to calculate the average marks of students using *args
def calculate_average(*marks):
    # Calculate the sum of all marks
    total = sum(marks)
    # Find the number of students
    num_students = len(marks)
    # Calculate the average
    average = total / num_students
    # Display the average
    print("Average Marks:", average)

    # Check if the student has passed or failed
    if average >= 50:
        print("The student has passed.")
    else:
        print("The student has failed.")


# Accepting student marks from the user
marks = input("Enter the marks of students separated by space: ").split()

# Converting the input to integers
marks = [int(mark) for mark in marks]

# Call the function with the user input
calculate_average(*marks)
# Function that accepts **kwargs (a dictionary of fruit names and their prices)
def display_fruit_keys(**kwargs):
    # Display only the keys (fruit names)
    print("Fruits Available:")
    for fruit in kwargs.keys():
        print(fruit)

# Call the function with a dictionary of fruit prices
display_fruit_keys(Mango=3, Apple=2, Orange=4)
# Function to calculate the average score of students using **kwargs
def calculate_avg_score(**kwargs):
    # Calculate the sum of all scores
    total_score = sum(kwargs.values())
    # Calculate the number of students
    num_students = len(kwargs)
    # Calculate the average
    average_score = total_score / num_students
    # Display the average score
    print("Average Score:", average_score)

# Passing student scores as keyword arguments
calculate_avg_score(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
import random

# Function to generate random numbers between 1 and 20 without repetition
def generate_random_numbers():
    numbers = random.sample(range(1, 21), 20)  # Generate 20 unique numbers from 1 to 20
    print("Random Numbers (1-20 without repetition):")
    print(numbers)

# Call the function
generate_random_numbers()
