class Counter:
      count:int = 0

      def __init__(self):
            Counter.count +=1

      @classmethod
      def show_count(cls):
            print(f"Object Created:{cls.count}")

count1 = Counter()
count2 = Counter()
count3 = Counter()
count4 = Counter()
count5 = Counter()
count6 = Counter()

Counter.show_count()



