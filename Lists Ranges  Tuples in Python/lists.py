# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrot_list = list(["non pinin", "no more", "a stiff", "bereft of life"])
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The lists contain the same items")
# else:
#     print("The lists contain different items")

# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)


# another_even = list(even)
#
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(even)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if "spam" not in meal:
        for food in meal:
            print(food)
