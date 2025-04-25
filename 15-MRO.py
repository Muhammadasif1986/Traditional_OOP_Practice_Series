class A:
      """
      Agar same method multiple parents me ho, to Python kis order me check karega
      """
      def show(self):
            print("Class A")
class B(A):
      def show(self):
            print("Class B")

class C(A):
      def show(self):
            print("Class C")


class D(C,A):
           pass

a= A()
b=B()
c=C()
d=D()

d.show()


print(a.__doc__)