try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    print("What kind of operation do you want to perform. " \
    "Press * for multiplication\n Press / for division\nPress + for addition\nPress - for substraction")
    
    o = input("Enter operation: ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            print(f"The result is {a / b}")
        case _:
            print("There is an Error")

except Exception as e:
    print("Enter a valid value of a and b")

