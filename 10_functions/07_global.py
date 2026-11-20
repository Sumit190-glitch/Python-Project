def sum(a , b):
    c = a + b
    global z
    z = 10
    return c
z = 20
print(sum(z,5))
print(z)    