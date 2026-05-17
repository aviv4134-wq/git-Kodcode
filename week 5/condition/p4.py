user_input_password = input('enter the password: ')
password = '12345678'
if  (user_input_password == password):
    print('access granted')
elif user_input_password != password and len(user_input_password) < 8 :
    print('too short')
else:
    print('wrong password')
