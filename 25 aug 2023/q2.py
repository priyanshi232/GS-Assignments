try:
    num = float(input("Enter a number: "))
    print(f"You entered: {num}")
except KeyboardInterrupt:
    print("\nUser canceled the input.")
except ValueError:
    print("Error: Please enter a valid number.")