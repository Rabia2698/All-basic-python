i = 2

while i < 3:
    print("loop iteration:", i)
    i += 1  
# This code demonstrates the use of a while loop in Python.
# It starts with i = 2 and continues to print the current value of i until it reaches 10.
# The output will be 2 to 9.

while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print("You entered:", user_input)
# This code demonstrates the use of a while loop to continuously prompt the user for input.
# It will keep asking for a number until the user types 'exit'.
# The input is then printed back to the user.
# The loop will exit when the user types 'exit'.
