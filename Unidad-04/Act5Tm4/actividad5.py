from persistent import Persistent
import transaction
from ZODB import FileStorage, DB

# Definición de las clases
class Juguete(Persistent):
    def __init__(self, nombre, tipo, material, edad_recomendada, precio, id_distribuidor):
        self.nombre = nombre
        self.tipo = tipo
        self.material = material
        self.edad_recomendada = edad_recomendada
        self.precio = precio
        self.id_distribuidor = id_distribuidor  # ID del distribuidor

class Distribuidor(Persistent):
    def __init__(self, nombre_distribuidor, direccion, telefono):
        self.nombre_distribuidor = nombre_distribuidor
        self.direccion = direccion
        self.telefono = telefono

storage = FileStorage.FileStorage('1dam.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

# Verificar y crear  si no existen
if not hasattr(root, 'juguetes'):
    root['juguetes'] = {}
if not hasattr(root, 'distribuidores'):
    root['distribuidores'] = {}

# datos en Distribuidores
root['distribuidores']['Distribuidor1'] = Distribuidor("Distribuidor1", "Calle Principal 123", "111-222-333")
root['distribuidores']['Distribuidor2'] = Distribuidor("Distribuidor2", "Avenida Secundaria 456", "444-555-666")

root['juguetes']['Muñeca'] = Juguete("Muñeca", "Figurita", "Plástico", 3, 20.00, "Distribuidor1")
root['juguetes']['Peluche'] = Juguete("Peluche", "Animal", "Tela", 0, 15.00, "Distribuidor1")
root['juguetes']['Bloques'] = Juguete("Bloques de Construcción", "Juego de Mesa", "Madera", 2, 25.00, "Distribuidor2")

transaction.commit()
print("Datos insertados con éxito.")

distribuidor_a_consultar = "Distribuidor1"
print(f"\nJuguetes adquiridos al {distribuidor_a_consultar}:")
for juguete in root['juguetes'].values():
    if juguete.id_distribuidor == distribuidor_a_consultar:
        print(f"Nombre: {juguete.nombre}, Tipo: {juguete.tipo}, Material: {juguete.material}, "
              f"Edad recomendada: {juguete.edad_recomendada}, Precio: {juguete.precio}")

connection.close()
db.close()
