import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except ValueError:
            print("That is not a valid integer.")
        finally:
            print("The finally clause always executes")


num1 = get_int("Please enter first integer ")
num2 = get_int("Please enter second integer ")

try:
    print("{} divided by {} is {}".format(num1, num2, num1 / num2))
except ZeroDivisionError:
    print("Sorry, the universe doesn't allow division by zero.")
    sys.exit(2)
else:
    print("Division performed successfully")

