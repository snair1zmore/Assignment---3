def factorial(n):
    
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number to find its factorial: "))

result = factorial(number)

print(f"The factorial of {number} is {result}")