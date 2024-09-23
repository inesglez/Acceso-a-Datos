
def calcular_area(largo, ancho):
    return largo * ancho


largo = float(input("Introduce el tamaño del lado largo del rectángulo: "))
ancho = float(input("Introduce el tamaño del lado ancho del rectángulo: "))

area = calcular_area(largo, ancho)

print("El área del rectángulo es:" , area)
