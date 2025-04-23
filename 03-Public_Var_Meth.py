class Car:
      brand = "Alto"

      def __init__(self,brand):
            self.brand = brand
            

      def start(self):
            print(f"{self.brand} Car is Started from Self")

      # @classmethod
      # def start(cls):
      #       print(f"{cls.brand} Car is Started from Cls")

car1= Car("Toyota")
car2= Car("Civic")
car3= Car("Suzuki")

car1.start()
print(car1.brand)
car2.start()
print(car2.brand)
print(Car.brand)