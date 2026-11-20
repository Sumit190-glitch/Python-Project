def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                print("Can he won the match")
                func()
                print("He is Cooking right now can he can surpass everyone")
        return wrapper
    return decorator

@repeat(1)
def say_hello():
    print("That's crazy")

say_hello()