x = input('enter a number: ')
y = input('enter a number: ')
try:
    if x == 10 or x == 50 and y == 20 or y == 80:
        print('On the edge')
    elif 10<= x <=50 and 20 <= y <= 80:
        print('Inside the rectangle')
    else:
         print('Out side the rectangle')
except:
         print('only numbers allowed')