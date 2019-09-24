some_text = input("Enter text: ")
split_text = set(some_text)
split_text.discard(" ")
# vowels = {"a", "e", "i", "o", "u"}
vowels = frozenset("aeiou")
remaining_text = split_text.difference(vowels)
print(sorted(remaining_text))
