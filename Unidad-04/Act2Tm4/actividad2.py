from ZODB import FileStorage, DB
import transaction

class Juguete:
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

root.juguetes = []  

juguete1 = Juguete("Muñeca", "Figurita", "Plástico", 3, 20.00)  
juguete2 = Juguete("Peluche", "Animal", "Tela", 0, 15.00)        
juguete3 = Juguete("Bloques de Construcción", "Juego de Mesa", "Madera", 2, 25.00)  

root.juguetes.append(juguete1)
root.juguetes.append(juguete2)
root.juguetes.append(juguete3)

transaction.commit()

print("Lista de juguetes con edad recomendada de 3 años o más:")
for juguete in root.juguetes:
    if hasattr(juguete, 'edad_recomendada') and juguete.edad_recomendada >= 3:
        print(f"Nombre: {juguete.nombre}, Tipo: {juguete.tipo}, Material: {juguete.material}, "
              f"Edad Recomendada: {juguete.edad_recomendada}, Precio: {juguete.precio}")

connection.close()
db.close()
