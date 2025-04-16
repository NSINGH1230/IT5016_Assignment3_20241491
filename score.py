# Lab Activity – Expressions and Statements
# Program to classify score based on given flowchart

# Get score from user
score = int(input("Enter your score (0-100): "))

# Check if score is within valid range
if 0 <= score <= 100:
    if score >= 80:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    print("Invalid range")
