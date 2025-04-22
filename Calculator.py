def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def symbols_print():
    for symbol in symbols:
        print(symbol)

calculate = True

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

    num1 = int(input("Enter the first number: "))
    symbols_print()
    operator = input("Enter the operator: ")
    num2 = int(input("Enter the second number: "))

    result = symbols[operator](n1=num1, n2=num2)
    print(f"{num1} {operator} {num2} = {result}")

    calculate_with_result = True

    while calculate_with_result:
        again = input(f"To continue calculating with {result} type 'y', otherwise type 'n' to begin new calculation: ").lower()
        if again == "y":
            num1 = result
            symbols_print()
            operator = input("Enter the operator: ")
            num2 = int(input("Enter the second number: "))

            result = symbols[operator](n1=num1, n2=num2)

            print(f"{num1} {operator} {num2} = {result}")
        else:
            calculate_with_result = False
            print("\n" * 100)