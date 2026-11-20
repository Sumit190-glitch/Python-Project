# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
a = [1, 5, 6774, 748, 84, 20, 74]
new = list(filter(lambda  x: x>9, a)) #Except using the lamda you can use the is_greater_than_9 function
print(new)