
def mayor_de_dos(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))


mayor = mayor_de_dos(numero1, numero2)

print("El mayor de los dos números es:", mayor)
