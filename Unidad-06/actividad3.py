import mysql.connector
import logging

# Configuración de logs
logging.basicConfig(filename='databasemanager.log', level=logging.INFO, format='%(asctime)s - %(message)s')

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario",  
        password="usuario",
        database="1dam"
    )
    cursor = conexion.cursor()
    print("Conexión exitosa a la base de datos.")

    # 1. Configuración Inicial: Crear las tablas necesarias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        contacto VARCHAR(255) NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS herramientas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        tipo VARCHAR(255) NOT NULL,
        proveedor_id INT,
        FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
    )
    """)
    logging.info("Configuración inicial completada.")
    print("Tablas creadas con éxito.")

    # 2. Gestión de Proveedores
    # Crear proveedores
    proveedores = [
        ("Proveedor A", "123-456-789"),
        ("Proveedor B", "987-654-321")
    ]
    cursor.executemany("INSERT INTO proveedores (nombre, contacto) VALUES (%s, %s)", proveedores)
    conexion.commit()
    logging.info("Proveedores creados: Proveedor A y Proveedor B.")
    print("Proveedor creado: Proveedor A")
    print("Proveedor creado: Proveedor B")

    # Actualizar contacto del Proveedor A con el DNI
    dni = "77934336D" 
    cursor.execute("UPDATE proveedores SET contacto = %s WHERE nombre = 'Proveedor A'", (dni,))
    conexion.commit()
    logging.info(f"Contacto del Proveedor A actualizado al DNI: {dni}.")
    print(f"Proveedor actualizado: Proveedor A, Nuevo contacto: {dni}")

    # Eliminar al Proveedor B
    cursor.execute("DELETE FROM proveedores WHERE nombre = 'Proveedor B'")
    conexion.commit()
    logging.info("Proveedor B eliminado de la base de datos.")
    print("Proveedor eliminado: Proveedor B")

    # 3. Gestión de Herramientas
    # Obtener el ID del Proveedor A
    cursor.execute("SELECT id FROM proveedores WHERE nombre = 'Proveedor A'")
    proveedor_a_id = cursor.fetchone()[0]  
    cursor.fetchall()  

    # Agregar herramientas al Proveedor A
    herramientas = [
        ("Martillo", "Manual", proveedor_a_id),
        ("Taladro", "Eléctrico", proveedor_a_id)
    ]
    cursor.executemany("INSERT INTO herramientas (nombre, tipo, proveedor_id) VALUES (%s, %s, %s)", herramientas)
    conexion.commit()
    logging.info("Herramientas Martillo y Taladro agregadas al Proveedor A.")
    print("Herramienta creada: Martillo")
    print("Herramienta creada: Taladro")

    # Consultar herramientas del Proveedor A
    cursor.execute("SELECT nombre, tipo FROM herramientas WHERE proveedor_id = %s", (proveedor_a_id,))
    herramientas = cursor.fetchall()
    print("Herramientas de Proveedor A:")
    for herramienta in herramientas:
        print(f" - Herramienta: {herramienta[0]}, Tipo: {herramienta[1]}")
    logging.info("Herramientas del Proveedor A consultadas.")

    # Actualizar el tipo del Martillo a Reforzado
    cursor.execute("UPDATE herramientas SET tipo = 'Reforzado' WHERE nombre = 'Martillo'")
    conexion.commit()
    logging.info("Tipo de la herramienta Martillo actualizado a Reforzado.")
    print("Herramienta actualizada: Martillo, Nuevo tipo: Reforzado")

    # Eliminar la herramienta Taladro
    cursor.execute("DELETE FROM herramientas WHERE nombre = 'Taladro'")
    conexion.commit()
    logging.info("Herramienta Taladro eliminada de la base de datos.")
    print("Herramienta eliminada: Taladro")

except Exception as e:
    print(f"Ocurrió un error: {e}")
    
finally:
   
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
        logging.info("Conexión a la base de datos cerrada.")
