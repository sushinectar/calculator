# DICTIONARY
operation = {"+", "-", "*", "/"}

# DATA ENTRY
num1 = float(input("Type one number: "))
num2 = float(input("Type more one number: "))

choose = input("Which operation do you want to use (+, -, *, /): ")

# CONDITIONALS RESPECTING THE DICTIONARY
if choose == "+":
  print(num1 + num2)
elif choose == "-":
  print(num1 - num2)
elif choose == "*":
  print(num1 * num2)
elif choose == "/":
  print(num1 / num2)
else:
  print("Invalid operation.")
