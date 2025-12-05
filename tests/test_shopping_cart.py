from source.shopping_cart import add_item

def test_add_item():
    cart = []
    add_item(cart, "grapes")
    assert "grapes" in cart


def test_remove_item():
    pass

def test_remove_nonexistent_item():
    pass

def test_display_cart():
    pass