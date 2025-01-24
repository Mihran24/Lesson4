valid = False
while not valid :
    try:
        num = int(input("Enter A number: "))
        while num%2 == 0:
            print("Bye")
        valid = True
    except ValueError as ex:
        print("Invalid Input: ", ex)