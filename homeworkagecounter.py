valid = False
try:
    num = int(input("Enter A Number: "))
    while num%2 == 0:
        print("Age is odd")
except ValueError as ex:
        print("Invalid Input: ", ex)
        