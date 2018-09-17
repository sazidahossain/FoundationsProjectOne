####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Sprinkles"
signature_flavors = ["chocolate peanut butter", "chocolate sundae", "chocolate espresso"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for i in menu:
        print("-\" "+str(i) + " \" (" + str(menu[i]) + " KWD) ")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print("-\" "+i+" \"")


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print("-\" "+i+" \"")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    for i in menu:
        if order==i:
            return True
    for i in original_flavors:
        if order==i:
            return True
    for i in signature_flavors:
        if order==i:
            return True
    else:
        return False
def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("What's your order? (Enter the exact spelling of the items you want and type \'Exit\' to end your order"" )")
    orderx = input()
    while orderx != "Exit":
        if is_valid_order(orderx):
            order_list.append(orderx)
        orderx = input()

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for i in range(len(order_list)):
        for k in range(len(original_flavors)):
            if order_list[i] == original_flavors[k]:
                total = total+original_price
    for l in range(len(order_list)):
        for m in range(len(signature_flavors)):
            if order_list[l] == signature_flavors[m]:
                total = total+signature_price
    for t in range(len(order_list)):
        if order_list[t] == "tea":
            total = total+0.900
    for u in range(len(order_list)):
        if order_list[u] == "coffee":
            total = total+1
    for v in range(len(order_list)):
        if order_list[v] == "bottled water":
            total = total+0.750
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    price = get_total_price(order_list)
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print("- "+i)
    print("That'll be KD "+str(price))

    if accept_credit_card(price):
        print("This order is eligible for credit card payment. ")
    print("Thank you for shopping at "+cupcake_shop_name)
