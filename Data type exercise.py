# Get input from user
a = int(input("Enter an integer for a: "))
b = float(input("Enter a decimal number for b: "))
c = input("Enter a string for c: ")

# Create list, tuple, and dictionary for demonstration
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "John", "age": 30}

# Print data types
print("Data types:")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))
print("Type of f:", type(f))

# Convert b to string
b_str = str(b)
print("b as string:", b_str)
print("Type of b_str:", type(b_str))

# Exponential value of b
exp_b = b ** 2
print("b ** 2 =", exp_b)

# Modulus of a % 5
mod_result = a % 5
print("a % 5 =", mod_result)

# Assign operations on a
a += 5
print("a after += 5:", a)

