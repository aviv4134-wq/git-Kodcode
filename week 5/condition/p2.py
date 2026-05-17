
character_input = input('enter a one character: ')
if  not character_input.isalpha() or len(character_input) != 1:
     print('invalid')
elif character_input in ['a','e','i','o','u','A','E','I','O','U']:
      print('Vowel')
else:
      print('Consonant')
