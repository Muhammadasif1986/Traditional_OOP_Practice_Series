def log_function_call(func):
      """
      Decorator ek wrapper hota hai jo kisi \
 function ke andar ya pehle/baad kuch aur kaam karta hai.
      """
      def wrapper():
            print(f"{func.__name__} being called")
            func()
            print(f"{func.__name__} executed successfully")
                     
      
      return wrapper

@log_function_call
def say_hello():
      print("hello!")

say_hello()
print(log_function_call.__doc__)
