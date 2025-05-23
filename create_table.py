from tabulate import tabulate

# Simple example to create and display a table using tabulate


data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 28, "Teacher"]
]

headers = ["Name", "Age", "Profession"]

print(tabulate(data, headers=headers, tablefmt="grid"))