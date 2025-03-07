from statistics import multimode


def add(*numbers):
    list = [number for number in numbers]
    print(sum(list))

add(1,2,3,4,5,6,7,8,9)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        #self.make = kw["make"] # this is bad because whe we didn't set this value the method return error
        #self.model = kw["model"]
        self.model = kw.get("model") # This is correct because when we didn't set this value the method return none value
        self.make = kw.get("make")


my_car = Car()
my_second_car = Car(make="BMW")
my_third_car = Car(make="AUDI", model="A5")