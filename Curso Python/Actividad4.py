numero = int(input("Introduce un número entero: "))

# Mostrar la tabla de multiplicar desde el 1 hasta el 10
print("Tabla de multiplicar del" , numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


