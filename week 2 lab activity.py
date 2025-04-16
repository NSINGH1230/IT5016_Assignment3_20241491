# Ask user to enter the temperature in Celsius
temperature = float(input("Enter the temperature in Celsius: "))

# Check the temperature range and print the appropriate message
if temperature < 0:
    print("It's freezing!")
elif temperature >= 0 and temperature <= 15:
    print("It's cold!")
elif temperature >= 16 and temperature <= 30:
    print("It's warm!")
else:
    print("It's hot!")
import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

# Let the user try up to 5 times
while attempts < max_attempts:
    guess = int(input("Guess the number (between 1 and 20): "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break  # Exit the loop if guessed correctly

# If user fails to guess within 5 attempts
if guess != secret_number:
    print("Game over! The correct number was", secret_number)
# Print numbers from 1 to 50 with some conditions
for number in range(1, 51):
    if number > 40:
        break  # Stop the loop completely if number exceeds 40
    if number % 4 == 0:
        continue  # Skip numbers that are multiples of 4
    print(number)
