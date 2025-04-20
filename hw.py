# Program to calculate base^exponent using loop

# Input from user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

# Initialize result
result = 1

# Loop to calculate power
for _ in range(abs(exponent)):
    result *= base

# If exponent is negative, take reciprocal
if exponent < 0:
    result = 1 / result

# Display result
print(f"{base}^{exponent} = {result}")
