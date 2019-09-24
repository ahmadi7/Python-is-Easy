class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False

    def switch_powersource(self, source):
        self.power_source = source
    # def printit(self):
    #     print("Model: {}, Price: {}, Status: ".format(self.make, self.price, self.on))


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
# hamilton.printit()

# hamilton.printit()


print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characterisitcs.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_off()
print(kenwood.on)

print("-" * 80)
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch Kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

hamilton.switch_powersource("coal")
print(hamilton.power_source)