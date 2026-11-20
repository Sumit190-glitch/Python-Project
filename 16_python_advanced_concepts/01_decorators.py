def decorator(func):
    def wrapper():
        print("Enemies aare going to attack")
        func()
        print("Enemies are arrived on the spot")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

# f = decorator(say_hello) #can be able like this way also if you want
# f()
say_hello()