class Logger:
      def __init__(self):
           
            print(f"instance/Object is Created")


      def __del__(self):
            print(f"instance/Object is Deleted")

o1 = Logger()
del o1
