class Bank:
      bank_name = "BAHL"

      def __init__(self,account_name):
            self.account_name = account_name
      
      def display(self):
            print(f"Account Title is {self.account_name} {Bank.bank_name}")

      @classmethod
      def change_bank_name(cls,bank_name):
            cls.bank_name=bank_name
            print("you Bank name is changed {0}".format(bank_name,cls.bank_name))

b1 = Bank("Muhammad")      
b2 = Bank("Asif") 
b2.display()
b1.display()
b2.change_bank_name("Habib Metro")
b1.display()
