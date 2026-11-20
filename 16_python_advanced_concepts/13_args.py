def sum(*args):
#args is tuple of the all values passed to the sum 

    total = 0
    for item in args:
        total += item
    return total

print(sum(75, 20, 5, 90, 10, 75))