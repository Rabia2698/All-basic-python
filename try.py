number = input("Enter a number: ")

try:
    number = int(number)
    print("You entered a valid number:", number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
# This code demonstrates how to handle exceptions in Python using try-except blocks.
# It prompts the user to enter a number and attempts to convert it to an integer.
# If the conversion fails (e.g., if the user enters a non-numeric value), it catches the ValueError and prints an error message.
# This is a simple example of error handling in Python.