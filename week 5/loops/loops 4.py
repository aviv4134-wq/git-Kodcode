
vowels = ['a','e','i','o','u']
try:
    user_input = input('enter a word: ').lower()
    count_vowels = 0
    for w in user_input:
         if w in vowels :
             count_vowels += 1
    print(f'the count of vowels in {user_input} is {count_vowels}')
except:
    print('error please enter only words')

