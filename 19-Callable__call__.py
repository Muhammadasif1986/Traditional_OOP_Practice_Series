class Multiplier:
      """
      __call__:
Ek special method hai jo object ko function ki tarah call karne ki ability deta hai.
      """
      def __init__(self , factor):
            self.factor = factor

      def __call__(self , value):
           return self.factor * value

m = Multiplier(7)
print(callable(m))
print(m(7))
print(m.__doc__)