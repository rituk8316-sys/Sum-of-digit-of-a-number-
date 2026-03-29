# Program to find the sum of digits of a number
# id="s0dg1"

# Taking input from user
number = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Loop to calculate sum of digits
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

# Display result
print("Sum of digits is:", sum_of_digits)
