python_original = [1, 2, 3, 4, 5] # Result: [5, 4, 3, 2, 1]

print(python_original[::-1])
new_list = []
for i in range(len(python_original)-1,-1,-1):
    number = python_original[i]
    new_list.append(number)
print(new_list)