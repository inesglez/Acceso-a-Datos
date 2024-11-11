from ZODB import FileStorage, DB
import transaction
import persistent

class Juguete(persistent.Persistent):
    def __init__(self, nombre, tipo, material, edad_recomendada, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.material = material
        self.edad_recomendada = edad_recomendada 
        self.precio = precio

storage = FileStorage.FileStorage('1dam.fs')  
db = DB(storage)
connection = db.open()
root = connection.root

if not hasattr(root, 'juguetes'):
    root.juguetes = [] 

juguete1 = Juguete("Muñeca", "Figurita", "Plástico", 3, 20.00)
juguete2 = Juguete("Peluche", "Animal", "Tela", 0, 15.00)
juguete3 = Juguete("Bloques de Construcción", "Juego de Mesa", "Madera", 2, 25.00)

root.juguetes.append(juguete1)
root.juguetes.append(juguete2)
root.juguetes.append(juguete3)

transaction.commit()

juguete_a_modificar = root.juguetes[0]  # Recuperamos la primera instancia (Muñeca)

# Imprimir el valor del atributo antes del cambio
print(f"Antes de la modificación: Material de {juguete_a_modificar.nombre} es {juguete_a_modificar.material}")

# Modificar el atributo
juguete_a_modificar.material = "Plástico Reforzado"  # Cambiamos el material
transaction.commit()

print(f"Después de la modificación: Material de {juguete_a_modificar.nombre} es {juguete_a_modificar.material}")

connection.close()
db.close()
