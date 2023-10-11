class Product:
    def __init__(self, product_id, name, price, size, color):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.size = size
        self.color = color

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_from_cart(self, product):
        self.items = [item for item in self.items if item["product"] != product]

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart

    def place_order(self):
        # Simulate order placement (e.g., update inventory, payment processing)
        print("Order placed successfully!")

def main():
    product1 = Product(1, "Stylish Shirt", 29.99, "M", "Blue")
    product2 = Product(2, "Designer Jeans", 49.99, "L", "Black")

    customer = Customer("John Doe", "john@example.com")
    cart = ShoppingCart()
    
    cart.add_to_cart(product1, 2)
    cart.add_to_cart(product2, 1)
    
    print("Items in the cart:")
    for item in cart.items:
        print(f"{item['product'].name} - {item['quantity']} - ${item['product'].price}")

    total = cart.calculate_total()
    print(f"Total: ${total}")

    order = Order(customer, cart)
    order.place_order()

if __name__ == "__main__":
    main()
