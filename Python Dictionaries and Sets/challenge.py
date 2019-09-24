locations = {0: "You are sitting in front of a computer learning Python",
             1: "You have reached the End of the road",
             2: "You have climbed to the Top of hill",
             3: "You are Inside a building, a very large building",
             4: "You are in a Valley beside stream",
             5: "You are in the Forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
         "WEST": "W",
         "EAST": "E",
         "NORTH": "N",
         "SOUTH": "S"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))


loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + available_exits + " ").upper()
    print()

    # if direction in vocabulary.keys():
    #     direction = vocabulary[direction]
    #     loc = exits[loc][direction]
    # elif direction in exits[loc]:
    #     loc = exits[loc][direction]

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]

    else:
        print("You cannot go in that direction.")