try:
    user_score = int(input('enter a score: '))
    grade =    'A'  if 90 <= user_score <= 100 else('B' if 80<= user_score <= 89 else( 'C' if 70 <= user_score <= 79 else 'F') )
    print(grade)




except ValueError:
    print('enter only numbers')