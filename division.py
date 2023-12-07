# try except block - try catch block

class NegativeError(Exception):
    pass


try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError("No Negative numbers please")

    q = n / d

    print(q)

except ZeroDivisionError:
    print("Denominator cannot be zero")

except ValueError:
    print("Please type numbers only")

except NegativeError:
    print("Please don't input negative numbers")

except Exception as e:
    print(e)
    print("Something went wrong!!")

else:
    #WHenever try block is successfully executed without throwing any exceptions 
    print("I am else block")

finally:
    # This will run at the end whether any error was thrown or not
    print("I am finally block")


print("The end of the program")

# file handling example
# try:
    # Open a file 
    # Try to do something 
    # write into file - It may throw error 
#except:
    # Do something to handle error 
#finally: 
    # CLose the file 

