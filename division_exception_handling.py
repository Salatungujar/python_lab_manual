try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("The result is:", result)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
