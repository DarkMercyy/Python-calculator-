num1 = int(input("1 number: ")) 
print("add = +")
print("subtract = -") 
print("multiplication = *")
print("division = /")
op = input("Operator: ")
num2 = int(input("2 number: "))

if op == "+":
     print(num1 + num2)
elif op == "-":
     print(num1 - num2)
elif op == "/":
     print(num1 / num2)
elif op == "*":
     print(num1 * num2)
else:
     print("Invalid Operator") 
input('Press ENTER to exit')
