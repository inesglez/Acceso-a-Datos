
import random  
lista_numeros = [] #Crea lista vacia para almacenar los núm aleatorios

for i in range(10):  # range(10) genera una secuencia de 0 a 9
    #(10 iteraciones en total)

    numero_azar = random.randint(1, 50)
    # 'randint(1, 50)' genera un número entero aleatorio entre 1 y 50
    lista_numeros.append(numero_azar)

numero_usuario = int(input("Introduce un número en tre 1 y 50: "))  

if numero_usuario in lista_numeros:  
    print("¡Bingo!")
else:       
    print("Lo siento, el número no está en la lista.")
