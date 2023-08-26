def get_numerical_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a numerical value.")
try:
    num1 = get_numerical_input("Enter the first number: ")
    num2 = get_numerical_input("Enter the second number: ")
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except TypeError as e:
    print(f"Error: {e}")





