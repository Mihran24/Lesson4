try:
    val1, val2 = eval(input("Enter any Number : "))
    answer = val1 / val2
    print("Answer is", answer)
except ZeroDivisionError:
    print("Division by 0 is not possible!")
except SystemError as ex:
    print("SyntaxtError", ex)
except:
    print("Something Went Wrong")
else:
    print("All Cleared")
finally:
    print("This will not excecute no matter what and no matter how hard you try nobody cares")