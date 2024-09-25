
import random 

# lista vacía para guardar los números aleatorios
numeros_aleatorios = []

for i in range(10): 
    # Generar un número aleatorio entre 1 y 50 usando randint
    numero = random.randint(1, 50)  # random.randint(1, 50) genera
    #un número aleatorio entre 1 y 50 inclusive
    numeros_aleatorios.append(numero)

print(numeros_aleatorios)  


