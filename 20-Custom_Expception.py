class InvalidAgeError(Exception):
      """
      Make a custom class
      """
      pass

def check_age(age):
      if age < 18:
            raise InvalidAgeError("Age must be 18 or above")
      

try:
      check_age(15)
except InvalidAgeError as e:
      print(e)
