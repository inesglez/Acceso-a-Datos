from pymongo import MongoClient, errors

# Datos de Conexión
usuario = "usuario"
clave = "usuario"
base_datos = "1dam"
host = "localhost"
puerto = 27017

try:
    # Intento de conexión con MongoDB
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}", serverSelectionTimeoutMS=5000)
    
    # Selecciono la base de datos '1dam'
    db = client[base_datos]

    # Selecciono la colección de juguetes
    coleccion = db["Juguetes"]

    # 1. Añadir tres juguetes a la colección
    print("\nDocumentos en la colección antes de añadir juguetes:")
    for juguete in coleccion.find():
        print(juguete)

    nuevos_juguetes = [
        {"nombre": "Muñeca", "tipo": "Accesorio", "material": "Plástico", "edad_recomendada": 3, "precio": 19.99},
        {"nombre": "Pista de carreras", "tipo": "Vehículo", "material": "Madera", "edad_recomendada": 5, "precio": 29.99},
        {"nombre": "Construcción de bloques", "tipo": "Educativo", "material": "Plástico", "edad_recomendada": 4, "precio": 15.99}
    ]
    print("\n")
    for juguete in nuevos_juguetes:
        if not coleccion.find_one({"nombre": juguete["nombre"]}):
            coleccion.insert_one(juguete)
            print(f"Juguete '{juguete['nombre']}' insertado.")
        else:
            print(f"El juguete '{juguete['nombre']}' ya está en la colección.")

    print("\nDocumentos en la colección después de añadir los juguetes:")
    for juguete in coleccion.find():
        print(juguete)

    # 2. Actualizar el precio de un juguete (por ejemplo, de "Muñeca")
    coleccion.update_one({"nombre": "Muñeca"}, {"$set": {"precio": 22.99}})
    print("\nPrecio de 'Muñeca' actualizado.")

    # 3. Eliminar uno de los juguetes (por ejemplo, "Pista de carreras")
    coleccion.delete_one({"nombre": "Pista de carreras"})
    print("\nJuguete 'Pista de carreras' eliminado.")

    # Comprobación de las operaciones realizadas
    print("\nDocumentos en la colección después de las operaciones:")
    for juguete in coleccion.find():
        print(juguete)

except errors.ServerSelectionTimeoutError as err:
    # Este error ocurre si no puedo conectar con el servidor
    print(f"No se pudo conectar a MongoDB: {err}")
except errors.OperationFailure as err:
    # Este error ocurre si las credenciales son incorrectas o no tengo permisos suficientes
    print(f"Fallo en la autenticación o permisos insuficientes: {err}")
except Exception as err:
    # Cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {err}")
finally:
    # Cerrar la conexión si todo salió bien
    if 'client' in locals():
        client.close()
        print("Conexión cerrada.")
