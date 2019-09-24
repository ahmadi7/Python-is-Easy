# my_list = ["a", "b", "c", "d"]
#
# new_string = " - ".join(my_list)
#
# print(new_string)
#
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# letter_string = " - ".join(letters)
#
# print(letter_string)

# numbers = "123456789"
#
# new_string = " mississippi ".join(numbers)
#
# print(new_string)

locations = {0: "Computer",
             1: "End of road",
             2: "Top of hill",
             3: "Inside a building",
             4: "Valley beside stream",
             5: "Forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    # available_exits = ""
    # for direction in exits[loc].keys():
    #     available_exits += direction + ", "
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + available_exits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction.")