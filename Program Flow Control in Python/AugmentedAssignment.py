number = "9,223,372,036,854,775,807"
cleaned_number = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleaned_number += number[i]

newNumber = int(cleaned_number)
print("The number is {} ".format(newNumber))

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = "good "
greeting += "morning. "
print(greeting)

greeting *= 5
print(greeting)
