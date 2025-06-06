"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

Explaining properties.  Properties allow for reduction in Python code
and cleans up the user interface, making it more Pythonic.
"""

class Product:
    ##################### Unpythonic Way ########################
    # def __init__(self, price):                                #
    #    self.set_price(price)                                  #
    #                                                           #
    # def get_price(self):                                      #
    #     return self.__price                                   #
    #                                                           #
    # def set_price(self, value):                               #
    #     if value < 0:                                         #
    #         raise ValueError("Price cannot be negative.")     #
    #     self.__price = value                                  #
    #                                                           #
    # price = property(get_price, set_price)                    #
    #############################################################

    ##################### Pythonic Way ##########################
    def __init__(self, price):                                  #
        self.price = price                                      #
                                                                #
    @property                                                   #
    def price(self):                                            #
        return self.__price                                     #
                                                                #
    @price.setter                                               #
    def price(self, value):                                     #
        if value < 0:                                           #
            raise ValueError("Price cannot be negative:")       #
        self.__price = value                                    #
    #############################################################

# #################### Testing Unpythonic Way #####################
# # Declare and instantiate product and set it's price to 10      #
# product = Product(10)       # Price: 10                         #
# print(product)              # Object location in memory         #
# print(product.get_price())  # 10                                #
# print(product.price)        # 10                                #
# product.price = 20                                              #
# print(product.price)        # 20                                #
# print(product.get_price())  # 20                                #
# #################################################################

print()

##################### Testing Pythonic Way ######################
# Declare and instantiate product and set it's price to 10      #
product = Product(10)         # Price: 10                       #
# print(product.get_price())  # Error, no such method           #
print(product.price)          # 10                              #
# product.set_price(20)       # Error, no such method           #
product.price = 20                                              #
print(product.price)          # 20                              #
#print(product.get_price())   # Error, no such method           #
#################################################################
