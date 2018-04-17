#Singleton

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingleLocation(object):
    __metaclass__ = Singleton

    def printLocation(self):
        print(" Location " + self.__repr__() + "\n")


x = SingleLocation()
x.printLocation()

y = SingleLocation()
y.printLocation()

z = SingleLocation()
z.printLocation()

# correct print out:

# Location <__main__.SingleLocation object at 0x10bba3fd0>

# Location <__main__.SingleLocation object at 0x10bba3fd0>

# Location <__main__.SingleLocation object at 0x10bba3fd0>