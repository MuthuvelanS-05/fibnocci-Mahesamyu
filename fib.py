def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Take user input
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Generate and display the Fibonacci series
fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} terms:")
print(fib_series)
