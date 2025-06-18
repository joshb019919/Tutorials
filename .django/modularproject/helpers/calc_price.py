"""A reusable module to calculate the total price of a list of products
after tax and with any discount percent applied.
"""

def calc_price(products, tax, discount):
    """Return the cost of products with tax and discount applied.
    
    Parameters:
    products - a list of product objects with a price attribute.
    tax - a percent value without the percent sign (e.g., 6.78).
    discount - a percent value without the percent sign (e.g., 20.0).
    
    Return:
    A cost in US dollars.
    """
    return sum(products.price) * tax * discount / 1000
