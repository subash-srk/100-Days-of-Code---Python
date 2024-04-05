def add(*args):  # Unlimited Arguments
    res = 0
    for n in args:
        res += n
    print(args)
    print(type(args))
    print(res)


add(0, 1, 1, 2, 3)


# **Kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # print(kwargs["mul"])
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(2, add=3, mul=8)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car()
print(my_car.make)
print(my_car.color)



