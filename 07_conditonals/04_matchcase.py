a = (int(input("Enter the lucky number from 1 to 10:")))

match a:
    case 1:
        print("You won a grand prize")
    case 2:
        print("You are the second winner ")
    case 5:
        print("You are third winner")
    case _:
        print("Better luck next time")


          