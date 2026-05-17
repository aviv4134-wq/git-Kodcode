

password = '1234'
loop_flag = True
while loop_flag:
    user_input = input('enter the password: ')
    if user_input == password:
        print('Welcome')
        loop_flag = False
    else:
        print('Try again')
