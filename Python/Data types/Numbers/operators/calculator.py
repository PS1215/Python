#Our Calculator

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))

print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")