# Assignment-3
Module 4: Functions &amp; Modules in Python 

Task 1: Calculate Factorial Using a function

#Recursive function to calculate factorial of a number
def factorial(n):
    # Base case: factorial of 0 or negative numbers is 1
    if n < 1:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    else:
        return n * factorial(n - 1)

#Ask the user to enter a number
number = int(input("Enter a number to find its factorial: "))

#Call the factorial function and store the result
result = factorial(number)

#Print the result
print(f"The factorial of {number} is {result}")



TASK 2 - Using the math module to calculate
#Import the math module to use mathematical functions
import math

#Get input from the user and convert it to an integer
number = int(input("Enter a number: "))

#Mathematical Calculations

#Calculate the square root of the number
square_root = math.sqrt(number)

#Calculate the natural logarithm (base e) of the number
natural_log = math.log(number)

#Calculate the sine of the number in radians
sine_num = math.sin(number)

#Output

print(f"The square root of {number} is {square_root}")
print(f"The natural logarithm of {number} is {natural_log}")
print(f"The sine of {number} (in radians) is {sine_num}")
print("Thank You!")

