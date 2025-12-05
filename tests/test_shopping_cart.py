from source.shopping_cart import add_item, remove_item, display_cart

def test_add_item():
    cart = ["guava", "apple", "grapes"]
    add_item(cart, "mango")
    assert cart == ["guava", "apple", "grapes", "mango"]


def test_remove_item_success():
    cart = ["guava", "apple"]
    result = remove_item(cart, "apple")
    assert result == True
    assert cart == ["guava"]


def test_remove_nonexistent_item():
    cart = ["guava", "apple"]
    result = remove_item(cart, "mango")
    assert result == False
    assert cart == ["guava", "apple"]


def test_display_cart():
    cart = ["guava", "apple", "grapes", "mango"]
    output = display_cart(cart)
    assert output == ["1. guava", "2. apple", "3. grapes", "4. mango"]