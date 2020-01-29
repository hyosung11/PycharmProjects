# One method
# from utility import multiply, divide

# Another method - can avoid naming conflict e.g., 'max
# from shopping.more_shopping import shopping_cart

# if __name__ == '__main__':
#     print(shopping_cart.buy('apple'))
#     print(divide(5, 2))
#     print(multiply(5, 2))
#
#     print('please run this')

# RANDOM Built-in Module

# import random

# alternative import convention
# from random import shuffle
# import random as awesome # to avoid name collision

# import only what you need
# from random import shuffle
#
# my_list = [4,8,16,32,64]
# shuffle(my_list)
# print(my_list)


# SYS Built-in Module

# import sys
# #
# # sys.argv


# USEFUL MODULES
from collections import Counter, defaultdict, OrderedDict

# Counter: creates a dictionary that keeps track of occurrences
# li = [1,2,3,4,5,6,7,7]
# sentence = 'breath through the pain'
# print(Counter(sentence))

# defaultdict
# dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# print(dictionary['c'])

# OrderedDict()
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
#
# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1
#
# print(d2 == d)


# import datetime
#
# # print(datetime.time(2,45,55))
# print(datetime.date.today())


# LIST vs ARRAY
from array import array

arr = array('i', [1,23])

print(arr[0])



