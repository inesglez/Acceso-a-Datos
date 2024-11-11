from ZODB import FileStorage, DB
import transaction

storage = FileStorage.FileStorage('1dam.fs')  
db = DB(storage)
connection = db.open()
root = connection.root()

juguetes = [
    {"nombre": "Muñeca", "tipo": "Figurita", "material": "Plástico", "edad_recomendada": "3+", "precio": 20.00},
    {"nombre": "Peluche", "tipo": "Animal", "material": "Tela", "edad_recomendada": "0+", "precio": 15.00},
    {"nombre": "Bloques de Construcción", "tipo": "Juego de Mesa", "material": "Madera", "edad_recomendada": "2+", "precio": 25.00}
]

nombres_juguetes = [juguete["nombre"] for juguete in juguetes]
root.nombres_juguetes = nombres_juguetes  

transaction.commit()

print("Lista de juguetes almacenados:")
for nombre in root.nombres_juguetes:
    print(nombre)

connection.close()
db.close()
