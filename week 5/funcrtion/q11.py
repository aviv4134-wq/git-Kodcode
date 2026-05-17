
python_items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # Result: [3, 1, 4, 5, 9, 2, 6]


no_duplicats_list = []

for n in python_items:
    if n not in no_duplicats_list:
        no_duplicats_list.append(n)

print(no_duplicats_list)