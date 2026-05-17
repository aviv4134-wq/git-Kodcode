try:
    number_1 = int(input('enter a number: '))
    number_2 = int(input('enter a number: '))
    number_3 = int(input('enter a number: '))
    number_of_positive_numbers = bool(number_1 > 0) +  bool(number_2 > 0) + bool(number_3 > 0)
    print(f'the number of positives number is {number_of_positive_numbers} ')
except:
    print('enter only numbers')