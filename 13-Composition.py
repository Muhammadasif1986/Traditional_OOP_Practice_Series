class Engine:
    """
    "Jab ek class ke andar doosri class ka object hota hai, toh isay Composition kehte hain."

Yeh ek "Has-A" relationship hota hai.

Car has-a Engine

Laptop has-a Battery

Human has-a Heart
    """
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.is_started = False

    def start_car(self):
        if not self.is_started:
            self.engine.start()
            self.is_started = True
        else:
            print("Car is already started.")

    def stop_car(self):
        if self.is_started:
            self.engine.stop()
            self.is_started = False
        else:
            print("Car is already stopped.")
engine = Engine()
my_car = Car(engine)

my_car.start_car()   # Engine started.
my_car.start_car()   # Car is already started.
my_car.stop_car()    # Engine stopped.
my_car.stop_car()    # Car is already stopped.
