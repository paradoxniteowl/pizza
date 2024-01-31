"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Collin Poynor
"""

import order, checkout, inventory
from os import system

customer_order = []
while True:
    print("Welcome to Pizza Time!")
    print("Select an option below:")
    print("1. Order")
    print("2. Checkout")
    print("3. Exit")
    selection = input(">> ")
    if selection == "1":
        customer_order = order.start()
    elif selection == "2":
        if len(customer_order) > 0:
            checkout.start(customer_order)
        else:
            print("The cart is empty.")
    elif selection == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option; please enter a correct number")
        input("Press ENTER to continue")

system("cls")