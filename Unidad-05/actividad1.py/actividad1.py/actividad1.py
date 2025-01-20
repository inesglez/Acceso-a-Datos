from pymongo import MongoClient, errors

# Datos para conectarme a la base de datos
usuario = "usuario"
clave = "usuario"
base_datos = "1dam"
host = "localhost"
puerto = 27017

try:
    # Me conecto al servidor MongoDB con los datos que configuré
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}", serverSelectionTimeoutMS=5000)
    
    # Elijo la base de datos que quiero usar
    db = client[base_datos]

    # Intento listar las colecciones como prueba para asegurarme de que la conexión funciona
    colecciones = db.list_collection_names()

    print("Conexión exitosa. Aquí tienes las colecciones que encontré:")
    print(colecciones)
    
except errors.ServerSelectionTimeoutError as err:
    # Esto pasa si no se puede conectar al servidor dentro del tiempo permitido
    print(f"No pude conectarme a MongoDB: {err}")
except errors.OperationFailure as err:
    # Esto ocurre si la contraseña o el usuario están mal, o si no tengo permisos
    print(f"Hubo un problema con la autenticación o los permisos: {err}")
except Exception as err:
    # Aquí manejo cualquier otro error raro que pueda surgir
    print(f"Algo salió mal: {err}")
finally:
    # Cierro la conexión con MongoDB si todo salió bien
    if 'client' in locals():
        client.close()
        print("Conexión cerrada correctamente.")
