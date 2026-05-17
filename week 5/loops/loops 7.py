count_even = 0
user_input = 1234534
while user_input > 1:
    if user_input%10 % 2 == 0:
        count_even +=1
    user_input //= 10


print(count_even)