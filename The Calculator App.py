# Task 1
 
# def add_numbers():
#   addition =  number_1 + number_2
#   print(f"{number_1} + {number_2} = addition")
  
# def subtract_numbers():
#     subtraction = number_1 - number_2
#     print(f"{number_1} - {number_2} = subtraction")
   
# def multiply_numbers():
#     multiplication = number_1 * number_2
#     print(f"{number_1} * {number_2} = multiplication")
   
# def divide_numbers():
#     division = number_1 / number_2
#     if number_2 == 0:
#       print("Cannot divide by zero!")
#     else:
#       print(f"{number_1} / {number_2} = division")
     
# Task 2
# global variables
operation_type = input("What arithmetic operation would you like to perform? \n(Enter addition, subtraction, multiplication, or division) ")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


# Task 3 - Put it all together...
# functions
def add_numbers():
    addition =  number_1 + number_2
    print(f"{number_1} + {number_2} = {addition}")
  
def subtract_numbers():
    subtraction = number_1 - number_2
    print(f"{number_1} - {number_2} = {subtraction}")
   
def multiply_numbers():
    multiplication = number_1 * number_2
    print(f"{number_1} * {number_2} = {multiplication}")
   
def divide_numbers():
    if number_2 == 0:
      print("Cannot divide by zero!")
    else:
      division = number_1 / number_2
      print(f"{number_1} / {number_2} = {division}")
     
if operation_type == "addition":
  add_numbers()
elif operation_type == "subtraction":
  subtract_numbers()
elif operation_type == "multiplication":
  multiply_numbers()
elif operation_type == "division":
  divide_numbers()
else:
  print("This mathematical operation is not supported by this calculator.")