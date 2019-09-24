def build_tuple(*args):
    return args

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)


def word_length(*args):
    char_count = 0
    for word in args:
        char_count += len(word)
    return char_count / len(args)

def print_backwards(*args):
    for word in args[::-1]:
        print(word[::-1], end=' ')

def smallest(*args):
    return min(args)

print('Word length')
count = word_length("hello", "planet", "earth,", "take", "me", "to", "your", "leader")
print("The average word length is {}".format(count))
print()

print("Smallest")
lowest = smallest(9, 4, 56, 1, 5, -23, 84)
print("The smallest number is {}".format(lowest))
print()

print("Backwards")
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")