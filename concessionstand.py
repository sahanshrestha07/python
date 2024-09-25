menu={"pizza" : 3.00,
        "nachos" : 4.5,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00}
customer_cart = []
customer_total = 0
print("___MENU___")
for key,value in menu.items():
        print(f"{key}: {value}")
print("___MENU___")
while True :
        customer_order = input("Enter Your Order(enter q or quit to quit):")
        if customer_order == "q" or customer_order == "quit":
                break
        elif customer_order is not None:
                customer_cart.append(customer_order)
                customer_total += menu.get[customer_order]
                continue
order = " ".join(customer_cart)
print(f"Your order : {order}")
print(f"your cart is {customer_cart}")
print(f"your total is {customer_total}")
