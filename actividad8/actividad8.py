import pymysql
from pymysql import Error

try:
    conexion = pymysql.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='1dam'
    )
    if conexion.open:
        print("Conexión a la base de datos exitosa")

        # Creamos un cursor para interactuar con la base de datos 
        cursor = conexion.cursor()
        
        # Llamar al procedimiento almacenado
        nombre_juguete = "pelota"
        cursor.callproc("obtener_datos", (nombre_juguete, )) # La coma es necesaria para que se reconozca como una tupla
        
        # Obtener los múltiples conjustos de resultados
        # Al no existir el stored_reults() en pymysql llamamos directamente al fetchall()
        resultado = cursor.fetchall()
        for i in resultado:
            print(resultado)
        
        # Cerramos el cursor
        cursor.close()
except Error as e:
    print(f"Error de conexión: {e}")

finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")