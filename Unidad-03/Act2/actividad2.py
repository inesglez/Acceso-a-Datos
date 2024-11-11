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

# TAREA 1: Recuperar objetos de un tipo específico
def tarea1():
    print("Tarea1...")
    
    # Recuperar juguetes de tipo 'Peluche' (puedes cambiar el tipo según tu preferencia)
    juguetes_tipo_especifico = Juguetes.select().where(Juguetes.tipo == 'Peluche')
    
    # Mostrar dos atributos: nombre y precio
    for juguete in juguetes_tipo_especifico:
        print(f"Nombre: {juguete.nombre}, Precio: {juguete.precio}")

# TAREA 2: Eliminar un registro específico en base a dos atributos
def tarea2():
    print("Tarea2...")

    try:
        # Eliminar un juguete específico con nombre y material dados
        juguete_a_eliminar = Juguetes.get(Juguetes.nombre == 'Osito de peluche', Juguetes.material == 'Tela')
        juguete_a_eliminar.delete_instance()
        print(f"Juguete eliminado: {juguete_a_eliminar.nombre}")
    except Juguetes.DoesNotExist:
        print("El juguete no existe.")
    
    # Mostrar los juguetes restantes
    juguetes_restantes = Juguetes.select()
    for juguete in juguetes_restantes:
        print(f"Nombre: {juguete.nombre}, Material: {juguete.material}")

# TAREA 3: Eliminar varios registros que cumplan una condición
def tarea3():
    print("Tarea3...")

    # Eliminar todos los juguetes cuyo precio sea mayor a 25
    Juguetes.delete().where(Juguetes.precio > 25).execute()

    # Mostrar los juguetes restantes para verificar la eliminación
    juguetes_restantes = Juguetes.select()
    for juguete in juguetes_restantes:
        print(f"Nombre: {juguete.nombre}, Precio: {juguete.precio}")

# Función principal para ejecutar las tareas
def main():
    try:
        db.connect()  # Conectar a la base de datos
        print("Conectado a la base de datos.")
        
        tarea1()  # Ejecutar TAREA 1
        tarea2()  # Ejecutar TAREA 2
        tarea3()  # Ejecutar TAREA 3
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        db.close()  # Cerrar la conexión
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
