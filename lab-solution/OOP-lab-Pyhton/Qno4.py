# 4. Write a Python program to create a class representing a shopping cart.
# Create stock as class variable and check for out-of-stock while adding to card. 
# Include methods for adding and removing items, and calculating the total price for a cart.

class ShoppingCart:
    stock = {
        'apple': {'price': 1.0, 'quantity': 10},
        'banana': {'price': 0.5, 'quantity': 20},
        'orange': {'price': 0.8, 'quantity': 15}
    }
    
    def __init__(self):
        self.cart = {}
    
    def add_item(self, item, quantity):
        if item not in self.stock or self.stock[item]['quantity'] < quantity:
            print(f"Cannot add {quantity} {item}(s) to the cart. Check stock availability.")
            return
        self.stock[item]['quantity'] -= quantity
        self.cart[item] = self.cart.get(item, 0) + quantity
    
    def remove_item(self, item, quantity):
        if item not in self.cart or self.cart[item] < quantity:
            print(f"Cannot remove {quantity} {item}(s) from the cart. Check cart contents.")
            return
        self.cart[item] -= quantity
        if self.cart[item] == 0:
            del self.cart[item]
        self.stock[item]['quantity'] += quantity
    
    def calculate_total(self):
        return sum(self.stock[item]['price'] * quantity for item, quantity in self.cart.items())

# Example usage:
cart = ShoppingCart()
cart.add_item('apple', 3)
cart.add_item('banana', 5)
cart.add_item('orange', 2)
cart.add_item('banana', 16)  # Should print an out-of-stock message

print(f"Total price: ${cart.calculate_total():.2f}")

cart.remove_item('banana', 3)
print(f"Total price after removing items: ${cart.calculate_total():.2f}")
