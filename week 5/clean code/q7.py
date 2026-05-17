
TAX = 0.17


def process_cart(prices: list, quantities: list, usertype: str):
    total_price = 0
    # חישוב סכום הבסיס של כל המוצרים
    for index in range(len(prices)):
        price = prices[index]
        quantity = quantities[index]
        total_price += price * quantity

    #  הוספת המס
    total_price += total_price * TAX

    #  החלת הנחת מועדון
    if usertype == 'premium':
        total_price *= 0.9
    elif usertype == 'vip':
        total_price *= 0.8

    #  חישוב משלוח
    if total_price > 500:
        shipping = 0
    elif total_price > 200:
        shipping = 25
    else:
        shipping = 50

    total_price += shipping

    return total_price
prices = [5,10,120]
quantity = [4,7,10]
usertype = 'premium'
print(process_cart(prices,quantity,usertype))