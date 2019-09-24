# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("aren't you glad you got out?")

import random

highest = 100
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
tries = 0
while (guess != answer) and (tries <= 10):
    guess = int(input())
    tries += 1
    if guess == 0:
        break
    if guess < answer:
        print("Wrong. Please guess higher")
    elif guess > answer:
        print("Wrong. Please guess lower")
    else:
        print("Well done, you guessed it!")