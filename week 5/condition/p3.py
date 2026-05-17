age = 21
vip = 'no'
if age < 16:
    print('rejected')
elif age > 18 and vip == 'yes' or age in [19,20,21]:
    print('you can enter')
else:
    print('rejected')
