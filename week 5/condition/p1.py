age = input('enter your age: ')

try:
   age = int(age)
   if age <= 0 or age > 120:
      print(f'invalid age {age}')
   elif 0 < age <= 12:
       print('Teen')
   elif 13 <= age <= 17:
       print('Adult')
except ValueError:
    print('enter only numbers')