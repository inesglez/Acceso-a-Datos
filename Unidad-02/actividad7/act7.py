import pymysql
from pymysql import Error

try:
    # Conectar a la base de datos
    conexion = pymysql.connect(
        host="localhost",
        user="usuario",        # Cambia a tu usuario MySQL
        password="usuario",     # Cambia a tu contraseña MySQL
        database="1dam"         # La base de datos donde está la tabla Juguetes
    )

    # Crear un cursor
    cursor = conexion.cursor()

    # Iniciar la transacción
    print("Iniciando transacción...")

    # Insertar un nuevo registro en la tabla Juguetes
    sql_insert = """
    INSERT INTO Juguetes (id, nombre, tipo, edad_recomendada, precio, material)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Forzamos el error poniendo el id (int) como tipò string
    datos_juguetes = ('Pelota', 'Pelota', 'Deporte', 6, 5.50, 'Plástico') 

    # Ejecutar la consulta
    cursor.execute(sql_insert, datos_juguetes)

    # Hacer commit si todo va bien
    conexion.commit()
    print("Transacción exitosa: Registro insertado correctamente.")

except Error as e:
    # Si ocurre un error, hacer rollback
    print(f"Error en la transacción: {e}")
    if conexion:
        conexion.rollback()
        print("Se realizó rollback.")

finally:
    # Cerrar el cursor y la conexión si están abiertos
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
        print("Conexión cerrada.")
