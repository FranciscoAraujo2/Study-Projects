def calculator():
    # Get the mathematical expression from the user
    expression = input("Enter the mathematical expression: ")

    # Divide the expression into tokens using spaces as the separator
    tokens = expression.split(" ")

    # Initialize variables to store the operands
    num1 = int(tokens[0])
    num2 = int(tokens[2])

    # Identify the operator
    operator = tokens[1]

    # Perform the appropriate mathematical operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = None
        print("Invalid operator")

    # Print the result
    if result is not None:
        print("Result:", result)

# Call the calculator function
calculator()
