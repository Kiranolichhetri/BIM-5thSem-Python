x = int(input("Enter the number:"))

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3:
        print("x is three")
    case 4:
        print("x is four")
    case _ if x != 9:
        print("x is not 9")
    case _:
        print("x is", x)
