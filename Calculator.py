# Function for addition
def add(n1, n2):
    return n1 + n2 # Returns addition results

# Function for subtraction
def subtract(n1, n2):
    return n1 - n2 # Returns subtraction results

# Function for multiplying
def multiply(n1, n2):
    return n1 * n2 # Returns multiplication results

# Function for division
def divide(n1, n2):
    return n1 / n2 # Returns division results

# Dictionary with the operator symbols. Created for easier function calling.
symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Prints the symbol options before taking operations input.
def symbols_print():
    for symbol in symbols:
        print(symbol)

calculate = True

# A loop to continue prompting the user for calculations input.
while calculate:
    print(r"""
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """)

    num1 = int(input("Enter the first number: ")) # Prompt user for first number.
    symbols_print() # Prints the symbols for user to select from.
    operator = input("Enter the operator: ") # Prompts user to enter operator.
    num2 = int(input("Enter the second number: ")) # Prompts user for second number.

    result = symbols[operator](n1=num1, n2=num2) # Assigns user input as the function parameter values.
    print(f"{num1} {operator} {num2} = {result}")

    calculate_with_result = True

    # Loop to continue using the previous result in the calculations.
    while calculate_with_result:
        again = input(f"To continue calculating with {result} type 'y', otherwise type 'n' to begin new calculation: ").lower()

        # If user selects to continue calculation with previous result.
        if again == "y":
            num1 = result
            symbols_print()
            operator = input("Enter the operator: ")
            num2 = int(input("Enter the second number: "))

            result = symbols[operator](n1=num1, n2=num2)

            print(f"{num1} {operator} {num2} = {result}")
        # Exits the second loop and prompts user for initial inputs.
        else:
            calculate_with_result = False
            print("\n" * 100)