class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def turn_on(self):
        self.on = True
        # noinspection SpellCheckingInspection
        print("boiliiiingg")
        return None


kenwood = Kettle("plastic", 2750.10)

print(kenwood)
print(kenwood.price)

kenwood.price = 3000
print(kenwood.price)

arzum = Kettle("ceramic", 3400.99)
print(arzum.make)
arzum.turn_on()

print("Models: {0.make}".format(kenwood))
print(type(kenwood))
print(kenwood.power_source)
print(Kettle.power_source)

print(Kettle.__dict__)
kenwood.power = 20
print(kenwood.power)
