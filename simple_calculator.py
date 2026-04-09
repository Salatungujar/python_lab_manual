print("1.Add 2.Subtract 3.Multiply 4.Divide")
ch = int(input("Enter choice :"))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number :"))

if ch == 1:
    print("Add \nResult :", num1+num2)
elif ch == 2:
    print("Subteact \nResult :", num1-num2)
elif ch == 3:
    print("Multiply \nResult :", num1*num2)
elif ch == 4:
    print("Divide \nResult :", num1/num2)
else:
    print("Invalid choice")
