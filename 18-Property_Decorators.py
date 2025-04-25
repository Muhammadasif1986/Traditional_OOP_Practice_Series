class Product:
      def __init__(self,price):
            self.__price = price

      @property
      def price(self):
            return self.__price
      
      @price.setter
      def price(self , value):
            self.__price = value

      @price.deleter
      def price(self):
           del self.__price

prod = Product(100)
print(prod.price)
prod.price = 200
print(prod.price)
del prod.price


      