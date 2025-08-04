#Calculator

# This is a simple calculator program that performs basic arithmetic operations.

def add(x, y):
    return x + y

def sub(x, y):
    return x -y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {div(num1, num2)}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input")

calculator()