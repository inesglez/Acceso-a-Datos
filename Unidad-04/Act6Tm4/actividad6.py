from persistent import Persistent
import transaction
from ZODB import FileStorage, DB
import copy 

class Juguete(Persistent):
    def __init__(self, nombre, tipo, material, edad_recomendada, precio, id_distribuidor):
        self.nombre = nombre
        self.tipo = tipo
        self.material = material
        self.edad_recomendada = edad_recomendada
        self.precio = precio
        self.id_distribuidor = id_distribuidor  

class Distribuidor(Persistent):
    def __init__(self, nombre_distribuidor, direccion, telefono):
        self.nombre_distribuidor = nombre_distribuidor
        self.direccion = direccion
        self.telefono = telefono

storage = FileStorage.FileStorage('1dam.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'juguetes'):
    root['juguetes'] = {}
if not hasattr(root, 'distribuidores'):
    root['distribuidores'] = {}

root['distribuidores']['Distribuidor1'] = Distribuidor("Distribuidor1", "Calle Falsa 123", "123-456-789")
root['distribuidores']['Distribuidor2'] = Distribuidor("Distribuidor2", "Avenida Real 456", "987-654-321")

root['juguetes']['Juguete1'] = Juguete("Muñeca", "Muñeca", "Plástico", 3, 15.99, "Distribuidor1")
root['juguetes']['Juguete2'] = Juguete("Pelota", "Deporte", "Goma", 5, 9.99, "Distribuidor1")
root['juguetes']['Juguete3'] = Juguete("Rompecabezas", "Juego de mesa", "Cartón", 6, 12.49, "Distribuidor2")

transaction.commit()

juguete_original = root['juguetes']['Juguete1']
juguete_copia = copy.deepcopy(juguete_original)

juguete_copia.nombre = "Muñeca Modificada"
juguete_copia.precio = 19.99
juguete_copia.id_distribuidor = "Distribuidor2"

print("Detalles del juguete original:")
print(f"Nombre: {juguete_original.nombre}, Precio: {juguete_original.precio}, ID Distribuidor: {juguete_original.id_distribuidor}")

print("\nDetalles del juguete copiado y modificado:")
print(f"Nombre: {juguete_copia.nombre}, Precio: {juguete_copia.precio}, ID Distribuidor: {juguete_copia.id_distribuidor}")

distribuidor_original = root['distribuidores'][juguete_original.id_distribuidor]
print("\nDetalles del distribuidor original:")
print(f"Nombre: {distribuidor_original.nombre_distribuidor}, Dirección: {distribuidor_original.direccion}")

