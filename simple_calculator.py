from arithmetic import *

# Program's begin

print(">>> Saludos! esta es una calculadora básica con las operaciones de +, -, * y /")
print(">>> Por favor ingresa dos valores")
print("")

num2 = int(input("Primer numero: "))
num1 = int(input("Primer numero: "))

print("")

operation = input("Seleciona la operación (+, -, *, /): ")

print("")

# Result

result =  machine[operation](num1, num2)
print(f"Resultado: {result}")

print(">>> Fin del proceso~~")