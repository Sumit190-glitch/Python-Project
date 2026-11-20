a = int(input("Enter the 1st value"))
b = int(input("Enter the 2nd value"))

def divide (a, b):
    try:
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    finally:
        print("Hey this will always printed")

divide(a,b)

