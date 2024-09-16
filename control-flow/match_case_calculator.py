num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Choose the operation (+, -, *, /): ")
if choice == "+":
    print(f"The result is {num1 + num2}.")
elif choice == "-":
    print(f"The result is {num1 - num2}.")
elif choice == "*":
    print(f"The result is {num1 * num2}.")
elif choice == "/":
    if num2 > 0:
        print(f"The result is {num1 / num2}.")
    else:
        print("Cannot divide by zero.")