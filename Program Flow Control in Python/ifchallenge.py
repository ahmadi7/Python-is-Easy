name = input("What is your name? ")
age = int(input("How old are you, {0}? ".format(name)))

if age < 18:
    print("Sorry, you are too young for this holiday")
elif age > 30:
    print("Sorry, you are too old for this holiday")
else:
    print("Welcome to the holiday, {0}".format(name))
