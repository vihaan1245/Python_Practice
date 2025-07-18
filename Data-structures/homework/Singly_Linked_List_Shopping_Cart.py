# Online Shopping Cart (Singly Linked List)
# Scenario:
# Design a shopping cart where items are added as users browse the website. Users can remove items from the cart, and the total price should be calculated dynamically.
#
# Task:
#
# Implement a ShoppingCart class using a singly linked list.
# Each node represents an item with name and price.
# Create methods to:
# Add an item (add_item(name, price)).
# Remove an item by name (remove_item(name)).
# Calculate total cost (calculate_total()).
# Display items in the cart (display_cart()).
class Node:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None

class ShoppingCart:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_item(self, name, price):
        new_item = Node(name,price)
        if self.is_empty():
            self.head = new_item
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_item
        self.length += 1

    def remove_item(self, name):
        if self.is_empty():
            print("Your shopping cart is empty, nothing to remove")
        else:
            temp = self.head
            if temp.name == name:
                self.head = self.head.next
                self.length -= 1
            else:
                while temp.next.name != name:
                    temp = temp.next
                if temp.next:
                    temp.next = temp.next.next
                    self.length -= 1
                else:
                    print("Value not found")

    def calculate_total(self):
        if self.is_empty():
            bill = 0
            print(f"Your total is {bill}")
        else:
            total = 0
            temp = self.head
            while temp:
                total += temp.price
                temp = temp.next
            print(f"Your total bill is {total}$. Have a good day!")

    def display_cart(self):
        if self.is_empty():
            print("Cart is empty.")
        else:
            temp = self.head
            for _ in range(self.length):
                print(f"{temp.name}",end=" -> ")
                temp = temp.next

    def search_cart(self,name):
        if self.is_empty():
            print("Cart is empty")
            return

        temp = self.head
        while temp:
            if temp.name == name:
                print(f"\nItem in the cart has been found : {name}")
                return name
            temp = temp.next

        print()
        print("Item not found")




shopping = ShoppingCart()
shopping.add_item("Heinz",0.50)
shopping.add_item("Broccoli",3.50)
shopping.add_item("Pizza",1.50)
shopping.add_item("Chicken",4.50)
shopping.remove_item("Heinz")
shopping.calculate_total()
shopping.display_cart()
shopping.search_cart("Broccoli")

