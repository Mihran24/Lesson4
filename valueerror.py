try:
    number = int(input("Enter Any Number"))
    print("Here is the number: ", number)
except ValueError as ex :
    print("Exception", ex)