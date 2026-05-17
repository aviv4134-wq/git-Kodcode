

def factorial(n:int) ->int:
    factorial_number = 1
    for i in range(1,n+1):
        factorial_number *= i
    return factorial_number

print(factorial(4))