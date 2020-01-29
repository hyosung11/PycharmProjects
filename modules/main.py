# One method
from utility import multiply, divide

# Another method - can avoid naming conflict e.g., 'max
from shopping.more_shopping import shopping_cart

print(shopping_cart.buy('apple'))
print(divide(5, 2))
print(multiply(5, 2))

