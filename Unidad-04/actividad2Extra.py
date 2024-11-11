import transaction
from ZODB import FileStorage, DB
from persistent import Persistent  # Importar la clase Persistent

# clase Movil
class Movil(Persistent):  # Hereda de Persistent para hacer los objetos persistentes
    def __init__(self, marca, modelo, anio_lanzamiento, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.anio_lanzamiento = anio_lanzamiento
        self.sistema_operativo = sistema_operativo


storage = FileStorage.FileStorage('moviles.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

if not hasattr(root, 'moviles'):
    root.moviles = {}


def almacenar_moviles():
    movil1 = Movil("Apple", "iPhone 14", 2022, "iOS")
    movil2 = Movil("Samsung", "Galaxy S22", 2022, "Android")
    movil3 = Movil("Xiaomi", "Redmi Note 11", 2022, "Android")

    root.moviles['movil1'] = movil1
    root.moviles['movil2'] = movil2
    root.moviles['movil3'] = movil3

    transaction.commit()

def consultar_moviles(sistema_operativo_filtro):
    print(f"Moviles con sistema operativo {sistema_operativo_filtro}:")
    for key in root.moviles.keys():
        movil = root.moviles[key]
        if hasattr(movil, 'sistema_operativo') and movil.sistema_operativo == sistema_operativo_filtro:
            print(f"Marca: {movil.marca}, Modelo: {movil.modelo}, Año: {movil.anio_lanzamiento}, SO: {movil.sistema_operativo}")

def main():
    almacenar_moviles()
    consultar_moviles("Android")  

if __name__ == "__main__":
    main()

    connection.close()
    db.close()
