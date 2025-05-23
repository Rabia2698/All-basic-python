name_list = ['Alice', 'Bob', 'Charlie']
print(name_list)  # Output: ['Alice', 'Bob', 'Charlie']

name_list.append('David')
print(name_list)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

for name in name_list:
    print(name)

for i in range(len(name_list)):
    print(name_list[i])