# Class Decorator
def add_greeting(cls):
    """
    Class decorator ek function hai jo kisi class ko \
modify karta hai, jaise usme naye methods add karna, \
 bina class ka code change kiye.
    """
    def greet(self):
        return f"{self.name} Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Ali")
print(p.greet())
print(p)
print(add_greeting.__doc__)
