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

try:
    juguete1 = Juguete("Muñeca", "Figurita", "Plástico", 3, 20.00)
    juguete2 = Juguete("Peluche", "Animal", "Tela", 0, 15.00)
    juguete3 = Juguete("Bloques de Construcción", "Juego de Mesa", "Madera", 2, 25.00)

    root.juguetes.append(juguete1)
    root.juguetes.append(juguete2)
    root.juguetes.append(juguete3)
    transaction.commit()
    print("Transacción completada y cambios confirmados.")

except Exception as e:
    transaction.abort()
    print(f"Error al agregar juguetes: {e}. Transacción revertida.")
    
#mostrar juguetes
print("\nLista de juguetes almacenados:")
for juguete in root.juguetes:
    print(f"Nombre: {juguete.nombre}, Tipo: {juguete.tipo}, Material: {juguete.material}, "
          f"Edad recomendada: {juguete.edad_recomendada}, Precio: {juguete.precio}")

connection.close()
db.close()
