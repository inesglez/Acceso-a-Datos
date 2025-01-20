
from ZODB import DB, FileStorage
from persistent import Persistent
import transaction

# Clases parom ZODB import DB, FileStorage
from persistent import Persistent
#importa Libros y Prestamos
class Libros(Persistent):
    def __init__(self, id, titulo, autor, anio_publicacion, genero):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.genero = genero

class Prestamos(Persistent):
    def __init__(self, libro_id, nombre_usuario, fecha_prestamo, fecha_devolucion):
        self.libro_id = libro_id
        self.nombre_usuario = nombre_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

# Conectar a la base de datos ZODB
storage = FileStorage.FileStorage('1dam.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

# Verificar y crear colecciones si no existen
if 'libros' not in root:
    root['libros'] = {}

if 'prestamos' not in root:
    root['prestamos'] = {}

# Insertar datos en Prestamos
root['prestamos']['Prestamo1'] = Prestamos(1, "Juan Perez", "2023-10-01", "2023-11-01")
root['prestamos']['Prestamo2'] = Prestamos(2, "Ana Lopez", "2023-09-15", "2023-10-15")
root['prestamos']['Prestamo3'] = Prestamos(4, "Maria Gomez", "2023-09-20", "2023-10-20")

# Insertar datos en Libros
root['libros']['1'] = Libros(1, "Cien años de soledad", "Gabriel García Márquez", 1967, "Novela")
root['libros']['2'] = Libros(2, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela")
root['libros']['3'] = Libros(3, "El Principito", "Antoine de Saint-Exupéry", 1943, "Infantil")
root['libros']['4'] = Libros(4, "Crónica de una muerte anunciada", "Gabriel García Márquez", 1981, "Novela")
root['libros']['5'] = Libros(5, "1984", "George Orwell", 1949, "Distopía")
print("Libros añadidos correctamente a la base de datos")

# Confirmar la transacción
transaction.commit()


#3 consultar por género del libro
genero_deseado = "Novela"
for clave, libros in root['libros'].items():
    if hasattr(libros, 'genero') and libros.genero == genero_deseado:
        print(f"Id: {libros.id}, Nombre: {libros.titulo}, autor: {libros.autor}, año de publicacion: {libros.anio_publicacion}, genero: {libros.genero}, prestamo: {libros.fecha_prestamo}")


#4 transaccion
# Función para gestionar la inserción de varios prestamos con transacción
def agregar_prestamos():
    try:
        print("Iniciando la transacción para agregar prestamos...")
        # Verificar y crear 'prestamos' en root si no existe
        if 'prestamos' not in root:
            root['prestamos'] = {} # Inicializar una colección de prestamos si no existe
            transaction.commit() # Confirmar la creación en la base de datos
        # Crear y añadir nuevos prestamos
        prestamo4 = Prestamos(5, "Ines", "2023-10-01", "2023-11-01")
        prestamo5 = Prestamos(6, "Paula", "2023-05-10", "2023-06-10")
        prestamo6 = Prestamos(7, "Alberto", "2023-11-28", "2023-12-28")
        # Añadir prestamos a la colección en la raíz de ZODB
        root['prestamos']["Ines"] = prestamo4
        root['prestamos']["Paula"] = prestamo5
        root['prestamos']["Alberto"] = prestamo6
        # Confirmar la transacción
        transaction.commit()
        print("Transacción completada: Prestamos añadidos correctamente.")
    except Exception as e:
        # Si ocurre un error, revertimos la transacción
        transaction.abort()
        print(f"Error durante la transacción: {e}. Transacción revertida.")

# Llamar a la función para añadir mascotas
agregar_prestamos()

# Cerrar la conexión a la base de datos ZODB
connection.close()
db.close()

