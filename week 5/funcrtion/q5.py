def digital_root(n) ->list:
    list_of_digits = []
    n = str(n)
    for s in n:
        s= int(s)
        list_of_digits.append(s)
    return list_of_digits

def sum_digits(n):
    sum_of_digits = sum(digital_root(n))
    while sum_of_digits > 9:
          sum_of_digits=digital_root(sum_of_digits)
          sum_of_digits = sum(sum_of_digits)
    return sum_of_digits
print(sum_digits(123))
