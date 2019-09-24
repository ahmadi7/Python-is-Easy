fruit = {"orange": "a sweet, orange, citrus, fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# veg.update(fruit)
# print(veg)
#
# fruit.update(veg)
# print(fruit)
#
# print(fruit == veg)

fruit_copy = fruit.copy()
fruit_copy.update(veg)
print(fruit_copy)
print(fruit)
