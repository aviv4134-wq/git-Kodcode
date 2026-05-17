
def handle_purchase(user_email, product_name, product_price, stock, quantity):
    email_validation =  is_email_valid(user_email)
    if not email_validation:
        return None

    quantity_validation =  is_quantity_valid(quantity,stock)
    if not quantity_validation:
        return None

    final_price = caculated_discounts(product_price,quantity)
    stock = update_the_stock(quantity,stock)

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = final_price
    order_status = "confirmed"

    print_order_details(user_email, product_name, final_price, stock, quantity)
    return order_user, order_product, order_quantity, final_price, order_status

def is_email_valid(user_email):
    if not user_email:
        print("Invalid user")
        return False

def is_quantity_valid(quantity,stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False

def caculated_discounts(product_price,quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def update_the_stock(quantity,stock):
    stock -= quantity
    return stock

def print_order_details(user_email, product_name, final_price, stock, quantity):
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = final_price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
