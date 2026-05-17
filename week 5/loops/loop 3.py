


flag = True
list_of_names = []
while flag:
    user_input = input('enter a name product\nenter done when you finish:\n')
    if user_input == 'done':
        flag = False
    else:
        list_of_names.append(user_input)
print(*list_of_names)


for r in range(1,4):
    for c in range(1,4):
        if c == 2:
            break
        print(f'row: {r} col:{c} ')


