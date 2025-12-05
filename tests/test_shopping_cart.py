from source.shopping_cart import add_item

def test_add_item():
    cart = ["guava", "apple", "grapes"]
    add_item(cart, "mango")
    assert cart == ["guava", "apple", "grapes", "mango"]


def test_remove_item():
    pass


def test_remove_nonexistent_item():
    pass


def test_display_cart():
    pass