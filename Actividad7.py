
num = int(input("Ingresa un número del 1 al 7: "))

dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}


if 1 <= num <= 7:
    print("El día correspondiente es:" , dias_semana[num])
else:
    print("Número inválido. Debes ingresar un número entre 1 y 7.")
