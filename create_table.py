data = [["Alice", 24, "Engineer"],["Bob", 30, "Designer"],["Charlie", 28, "Teacher"]]

line_dash = "-" * len(f'{"Name":<10}{"Age":<5}{"Profession":<15}')
print(line_dash)
print(f'{"Name":<10}{"Age":<5}{"Profession":<15}')
print(line_dash)


for row in data:
    for i in range(len(data)):
        print(f'{row[i]:<10}', end='')
    print()
        #print(f'{row[0]:<10}{row[1]:<10}{row[2]:<10}')
print(line_dash)