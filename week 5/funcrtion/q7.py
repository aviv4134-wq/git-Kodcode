

def reverse_integer(number):

    number = str(number)
    reversed_number = ''
    if number[0] == '-':
        reversed_number+='-'
    for n in number[::-1]:
        if n == '0' or n == '-':
            continue
        reversed_number += n
    return int(reversed_number)

print(reverse_integer(20003400))
