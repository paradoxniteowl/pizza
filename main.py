"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Collin Poynor
"""

import order, checkout, inventory

print("Welcome to Pizza Time!")
print("Select an option below:")
print("1. Order")
print("2. Checkout")
print("3. Inventory")
print("4. Exit")

while True:
    selection = input(">> ")
    if selection == "1":
        order.start()
    elif selection == "2":
        checkout.start()
    elif selection == "3":
        inventory.start()
    elif selection == "4":
        break
    else:
        print("Invalid option; please enter a correct number")