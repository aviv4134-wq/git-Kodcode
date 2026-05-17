highest_number = 0
flag = True
while flag:
    try:
        user_number = int(input('enter a number:  '))
        if user_number == 0:
            flag = False
        elif highest_number < user_number:
             highest_number = user_number
    except ValueError:
        print('enter only a number')
print(f'the highest number is {highest_number}')