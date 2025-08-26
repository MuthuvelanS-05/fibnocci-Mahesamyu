# Function to calculate sum of first n numbers
def sum_of_n(n):
    return n * (n + 1) // 2  # Formula for sum of first n natural numbers

# Take user input
n = int(input("Enter a number: "))

# Calculate and display the sum
result = sum_of_n(n)
print(f"The sum of the first {n} numbers is: {result}")
