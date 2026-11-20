# while True:
#     try:      
#         a = int(input("Enter the value of the 1st element: "))
#         b = int(input("Enter the value of the 2nd element: "))

#         print(f"The sum is {a/b}")

#     except ZeroDivisionError:
#         print("Don't do that OR else just don't divide by the 0")

#     except ValueError:
#         print("Why you wasting my time BRUh..")
#     except Exception as e:
#         print("Some error occured!", e)

a = int(input("Enter the value of the 1st element: "))
b = int(input("Enter the value of the 2nd element: "))

if b == 1:
        raise ValueError("Hey can you stop it")


print(f"The sum is {a/b}")
            
            