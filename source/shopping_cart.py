cart = []

def add_item(cart, item):
    cart.append(item)
    return cart

def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
        return True
    return False

def display_cart(cart):
    return [f"{i}. {item}" for i, item in enumerate(cart, start=1)]
