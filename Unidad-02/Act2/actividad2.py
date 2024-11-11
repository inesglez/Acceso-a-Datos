import pymysql
from pymysql import Error

# Conexión a la base de datos MySQL
conexion = pymysql.connect(
    host="localhost",     # Cambia esto si tu base de datos está en otro servidor
    user="usuario",       # Tu usuario de MySQL
    password="usuario",   # Tu contraseña de MySQL
    database="1dam"       # Asegúrate de que la base de datos exista
)

cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Juguetes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        tipo VARCHAR(200), 
        edad_recomendada INT,
        precio FLOAT
    )
""")

# Insertar datos en la tabla
cursor.executemany(
    "INSERT INTO Juguetes (nombre, tipo, edad_recomendada, precio) VALUES (%s, %s, %s, %s)",
    [
        ('Lego Star Wars', 'Construcción', 8, 49.99),
        ('Barbie Dreamhouse', 'Muñecas', 5, 159.99),
        ('Hot Wheels Pista Turbo', 'Coches', 6, 29.99),
        ('Puzzle 1000 piezas', 'Rompecabezas', 10, 19.99),
        ('Nerf Blaster', 'Juguetes de acción', 7, 24.99),
        ('Pelota', 'Deportes', 3, 9.99)
    ]
)

# Confirmar los cambios
conexion.commit()

# Realizar una consulta para recuperar los datos
cursor.execute("SELECT * FROM Juguetes")

# Imprimir todos los registros
for fila in cursor.fetchall():
    print(fila)

# Cerrar la conexión
conexion.close()
