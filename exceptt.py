"""try:
    num=int(input("Enter number:"))
    result =10/num
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("invalid input")    """

try:
    num=int(input("Enter a number:"))
    result =100/num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("execution completed")            


 