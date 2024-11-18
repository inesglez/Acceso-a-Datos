from pymongo import MongoClient, errors

# Datos básicos para conectar a la base de datos
usuario = "usuario"
clave = "usuario"
base_datos = "1dam"
host = "localhost"
puerto = 27017

try:
    # Me conecto al servidor de MongoDB con los datos que configuré arriba
    client = MongoClient(f"mongodb://{usuario}:{clave}@{host}:{puerto}/{base_datos}", serverSelectionTimeoutMS=5000)
    
    # Entro a la base de datos que quiero usar
    db = client[base_datos]

    # Elijo la colección "Juguetes" porque ahí es donde tengo mis datos
    coleccion = db["Juguetes"]

    # 1. Busco juguetes para una edad específica
    # Aquí filtro los juguetes que son recomendados para niños de 3 años
    consulta = {"edad_recomendada": 3}
    juguetes = coleccion.find(consulta)

    print("Juguetes recomendados para niños de 3 años:")
    for juguete in juguetes:
        print(juguete)

    # 2. Solo quiero ver los nombres y precios de los juguetes
    # En este caso, oculto el ID y dejo que solo se vean los campos que me interesan
    proyeccion = {"_id": 0, "nombre": 1, "precio": 1}
    juguetes_proyectados = coleccion.find(consulta, proyeccion)

    print("\nNombres y precios de los juguetes:")
    for juguete in juguetes_proyectados:
        print(juguete)

    # 3. Limito los resultados y los ordeno por precio
    # Aquí tomo los 2 juguetes más caros para la edad de 3 años y los ordeno de mayor a menor precio
    juguetes_limitados_ordenados = coleccion.find(consulta, proyeccion).limit(2).sort("precio", -1)

    print("\nLos 2 juguetes más caros:")
    for juguete in juguetes_limitados_ordenados:
        print(juguete)

except errors.ServerSelectionTimeoutError as err:
    # Esto pasa si no puedo conectarme al servidor (el host o puerto están mal o algo así)
    print(f"No me pude conectar a MongoDB: {err}")
except errors.OperationFailure as err:
    # Esto ocurre si puse mal el usuario/contraseña o no tengo permisos
    print(f"Problema de autenticación o permisos: {err}")
except Exception as err:
    # Aquí capturo cualquier otro error raro que pueda pasar
    print(f"Algo salió mal: {err}")
finally:
    # Cierro la conexión porque ya terminé, así no dejo cosas abiertas
    if 'client' in locals():
        client.close()
        print("Cerré la conexión con la base de datos.")
