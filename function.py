def say_hello(name):
    """
    This function takes a name as an argument and prints a greeting message.
    """
    print(f'Hello {name.upper()}!')
# This code defines a function called say_hello that takes a name as an argument.

def add_numbers(a, b):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    print('Adding numbers:', a + b)
    return a + b    
# This code defines a function called add_numbers that takes two numbers as arguments and returns their sum.
# It demonstrates how to define and use functions in Python.
# The function is then called with different arguments to demonstrate its usage.

def multiply_numbers(a, b):
    pass
# This code defines a function called multiply_numbers that takes two numbers as arguments.
# The function is currently empty and does not perform any operations.
# It demonstrates how to define a function in Python without implementing its logic.

while True:
    user_name = input("Enter your name: ")
    say_hello(user_name)

    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    
    add_numbers(num_1, num_2)
    
    exit_choice = input("Do you want to exit? (yes/no): ").lower()
    
    if exit_choice == 'yes':
        print("Exiting the loop.")
        break
    else: 
        print("Continuing the loop.")
    