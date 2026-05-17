user_input  = input('enter a word: ')
reversed_word = ''
for w in range(len(user_input)-1,-1,-1):
    reversed_word += user_input[w]
print(reversed_word)