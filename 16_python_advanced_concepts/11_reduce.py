from functools import reduce

numbers = [1, 3, 4, 6, 7, 9, 5]
#         [4 ,4, 6, 7, 9, 5]
#         [8 , 6, 7, 9, 5]
#         [14, 7, 9, 5]
#         [21, 9, 5]
#         [30, 5]
#         [35]

def sum(a,b):
    return a+b

c = reduce(sum, numbers)
print(c)