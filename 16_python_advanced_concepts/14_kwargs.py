def marks(**kwargs):
#kwargs is the dictionary with all the key value pairs which were passed to marks function
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Sumit = 60, Harry = 100, Aman = 90)
