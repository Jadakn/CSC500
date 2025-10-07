try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Error: Please enter a numeric value for the first number.")
    exit()
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter a numeric value for the second number.")
    exit()
    
print("The sum is:", num1 + num2)
print("The difference is:", num1 - num2)
print("The product is:", num1 * num2)
try:
    print("The quotient is:", num1 / num2)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
