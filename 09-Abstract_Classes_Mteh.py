from abc import ABC , abstractmethod

class Shape(ABC):

      @abstractmethod
      def area(self):
            pass

class Rectangle(Shape):
      def __init__(self,width,length):
            self.width = width
            self.length = length

      def area(self):
            return self.width * self.length
      
re = Rectangle(3,9)
print(re.area())


