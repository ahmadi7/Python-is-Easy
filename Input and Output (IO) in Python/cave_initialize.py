import shelve

cave_data = shelve.open("cavedata")
cave_data["locations"] = {0: {"desc": "You are sitting in front of a computer learning Python",
                              "exits": {},
                              "named_exits": {}},
                          1: {"desc": "You have reached the End of the road",
                              "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                              "named_exits": {"2": 2, "3": 3, "4": 4, "5": 5}},
                          2: {"desc": "You have climbed to the Top of hill",
                              "exits": {"N": 5, "Q": 0},
                              "named_exits": {"5": 5}},
                          3: {"desc": "You are Inside a building, a very large building",
                              "exits": {"W": 1, "Q": 0},
                              "named_exits": {"1": 1}},
                          4: {"desc": "You are in a Valley beside stream",
                              "exits": {"N": 1, "W": 2, "Q": 0},
                              "named_exits": {"2": 2, "1": 1}},
                          5: {"desc": "You are in the Forest",
                              "exits": {"W": 2, "S": 1, "Q": 0},
                              "named_exits": {"1": 1, "2": 2}}
                          }

cave_data["vocabulary"] = {"QUIT": "Q",
                           "WEST": "W",
                           "EAST": "E",
                           "NORTH": "N",
                           "SOUTH": "S",
                           "ROAD": "1",
                           "HILL": "2",
                           "BUILDING": "3",
                           "VALLEY": "4",
                           "FOREST": "5"}

cave_data.close()
