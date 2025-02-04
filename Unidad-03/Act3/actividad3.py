from peewee import MySQLDatabase, Model, CharField, IntegerField, FloatField, AutoField

# Conexión a la base de datos MySQL
db = MySQLDatabase('1dam', user='usuario', password='usuario',
                   host='localhost', port=3306)

# Definir el modelo de la tabla Juguetes
class Juguetes(Model):
    id = AutoField()  # Clave primaria autoincremental
    nombre = CharField()  
    tipo = CharField()   
    material = CharField() 
    edad_recomendada = IntegerField()  
    precio = FloatField() 

    class Meta:
        database = db  # Conexión a la base de datos
        table_name = 'Juguetes'  # Nombre de la tabla

# Función para insertar registros con una transacción
def insertar_registros_con_transaccion():
    juguetes = [
        {'nombre': 'Muñeca', 'tipo': 'Accesorio', 'material': 'Plástico', 'edad_recomendada': 3, 'precio': 19.99},
        {'nombre': 'Pista de carreras', 'tipo': 'Vehículo', 'material': 'Madera', 'edad_recomendada': 5, 'precio': 29.99},
        {'nombre': 'Construcción de bloques', 'tipo': 'Educativo', 'material': 'Plástico', 'edad_recomendada': 4, 'precio': 15.99},
        {'nombre': 'Osito de peluche', 'tipo': 'Peluche', 'material': 'Tela', 'edad_recomendada': 2, 'precio': 25.99},
        {'nombre': 'Juego de mesa', 'tipo': 'Juego', 'material': 'Cartón', 'edad_recomendada': 6, 'precio': 34.99}
    ]

    try:
        with db.atomic():  # Inicia la transacción
            for juguete in juguetes:
                Juguetes.create(**juguete)
            print("Registros insertados correctamente.")
    except Exception as e:
        print(f"Error durante la inserción: {e}")
        # La transacción se revierte automáticamente si ocurre un error

# Función principal para ejecutar el script
def main():
    try:
        db.connect()  # Conectar a la base de datos
        print("Conectado a la base de datos.")
        
        insertar_registros_con_transaccion()  # Insertar registros con transacción
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()  # Cerrar la conexión
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
