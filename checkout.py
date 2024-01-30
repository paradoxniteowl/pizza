def start(order):
    subtotal = 0
    tax_rate = 0.095
    print("Customer order: ")
    for i in order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price
    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Total: $" + str(round(tax + subtotal, 2)))
    payment(total)
    input("Press ENTER to continue")
    #get total price
    #add tax
    #accept payment
    #give change
    print("This is the checkout system")

def payment(total):
    while True:
        payment_type = input("Cash or credit? ")
        if payment_type.lower() == "cash":
            print(f"Your total is ${total}")
            cash = int(input("Enter cash received: "))
            change = cash - total
            print(f"Return ${change} to the customer.")
            input("Press ENTER to continue")
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Please swipe credit card")
            input("Press ENTER to continue")
            break
        else:
            print("Please enter cash or credit only")