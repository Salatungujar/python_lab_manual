num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter the third number :"))
if num1>num2 and num2>num3:
    print("Largest : ", num1)
elif num2>num3:
    print("Lagest : ", num2)
else:
    print("Largest :", num3)
