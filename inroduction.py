def perform_operation(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        return result
    elif operation == '-':
        result = num1 - num2
        return result
    elif operation == '*':
        result = num1 * num2
        return result
    elif operation == '/':
        # Ensure second number is not zero to avoid division by zero error
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return None

# Prompt the user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and print the result
result = perform_operation(num1, num2, operation)
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
