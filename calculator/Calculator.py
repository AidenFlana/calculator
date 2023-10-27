import math


# Outputs the menu
def menu():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("Welcome to the Calculator App")
  print("Please select an option:")

  print("0. Manuel")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Square Root")
  print("6. Exponent")
  print("7. Absolute Value")
  print("8. Trigonometry Functions")
  print("9. Natural Log")
  print("10. Logarithm")
  print("11. Factorial")
  print("12. pi")
  print("13. e")
  print("X. Exit")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  choice = input("Enter your choice(input number): ")
  return choice
#adds the inputs
def add(x, y):
  return x + y

#subtracts the inputs
def subtract(x, y):
  return x - y

#multiplies the inputs
def multiply(x, y):
  return x * y

#divides the inputs
def divide(x, y):
  return x / y
  
# Square roots the inputs
def square_root(x):
  return math.sqrt(x)

# Raises the inputs to the power of input
def exponent(x, y):
  return math.pow(x, y)

# Takes the absolute value of the inputs
def absolute_value(x):
  return abs(x)

# returns trig values
def Trigonometry_Functions(x):
  return math.sin(x), math.cos(x), math.tan(x)
def arc_trig(x):
  return math.asin(x), math.acos(x), math.atan(x)
# Takes the natural log of the input
def ln(x):
  return math.log(x)

# Takes the log of the input using another input as its base
def log(x, base):
  return math.log(x, base)
# returns factorial of input
def factorial(x):
  return math.factorial(x)
# returns pi
def pi():
  return math.pi
# e is Euler's number
def e():
  return math.e
# Calls the function based on the choice and loops through until exit is chosen
def main():
  while True:
      choice = menu()#Displays th menu
      if choice == "0":
        file = open("Manual.txt", "r")#reads the manual then prints it if called.
        print(file.read())
      elif choice == "X":
          break
      elif choice == "1":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = add(x, y)
        print(f"{x} + {y} = {result}")
          
      elif choice == "2":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = subtract(x, y)
        print(f"{x} - {y} = {result}")
        
      elif choice == "3":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = multiply(x, y)
        print(f"{x} * {y} = {result}")
        
      elif choice == "4":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = divide(x, y)
        print(f"{x} / {y} = {result}")
        
      elif choice == "5":
        x = float(input("Enter the number: "))
        result = square_root(x)
        print(f"Square root of {x} = {result}")
        
      elif choice == "6":
        x = float(input("Enter the base: "))
        y = float(input("Enter the exponent: "))
        result = exponent(x, y)
        print(f"{x} ^ {y} = {result}")
        
      elif choice == "7":
        x = float(input("Enter the number: "))
        result = absolute_value(x)
        print(f"Absolute value of {x} = {result}")
        
      elif choice == "8":
        function = input("Enter the function ('sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan'): ")
        if function == "sin" or function == "cos" or function == "tan":#for trig functions
          angle_degrees = float(input("Enter the angle in degrees: "))
          angle_radians = math.radians(angle_degrees)#converts radians to degrees
          result = Trigonometry_Functions(angle_radians)
          if function == "sin":
            print(f"Sine ({angle_degrees}) = {result[0]}")
          elif function == "cos":
            print(f"Cosine of ({angle_degrees}) = {result[1]}")
          elif function == "tan":
            print(f"Tangent of ({angle_degrees}) = {result[2]}")
        elif function == "arcsin" or function == "arccos" or function == "arctan":# for arc trig functions
          value = float(input("Enter the value: "))
          while value >= 1 and value <= -1:#makes sure entry is valid
            print("Value must be between -1 and 1")
            value = float(input("Try again enter the value: "))
          arc_radians = arc_trig(value)
          print(arc_radians)
          if function == "arcsin":
            print(f"Arc sine of {value} = {math.degrees(arc_radians[0])} degrees")
          elif function == "arccos":
            print(f"Arc cosine of {value} = {math.degrees(arc_radians[1])}degrees")
          elif function == "arctan":
            print(f"Arc tangent of {value} = {math.degrees(arc_radians[2])}degrees")
            #converts radians to degrees
      elif choice == "9":
        x = float(input("Enter the number: "))
        result = ln(x)
        print(f"ln({x}) = {result}")
        
      elif choice == "10":
        x = float(input("Enter the number: "))
        base = float(input("Enter the base: "))
        result = log(x, base)
        print(f"log{base}({x}) = {result}")
        
      elif choice == "11":
        x = float(input("Enter the number: "))
        result = factorial(x)
        print(f"Factorial of {x} = {result}")
        
      elif choice == "12":
        print(f"Pi = {pi()}")
        
      elif choice == "13":
        print(f"e = {e()}")
        
main()#runs calculator