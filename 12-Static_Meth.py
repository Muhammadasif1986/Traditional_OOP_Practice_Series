class Temp_convertor:
      @staticmethod
      def Celsius_fahrenheit(c):
            Temperature =  (c * 1.8 ) + 32
            rounded = round(Temperature , 2)
            return (f'{rounded} Fahrenheit')

      @staticmethod
      def Fahrenheit_Celsius(f):
            Temperature =  (f - 32 ) * 0.555
            rounded = round(Temperature , 2)
            return (f'{rounded} Fahrenheit')
      
tem_convertor = Temp_convertor()
print(tem_convertor.Celsius_fahrenheit(37))
print(tem_convertor.Fahrenheit_Celsius(98.6))
