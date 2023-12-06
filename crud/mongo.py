import pymongo

def connect():
    
    #Conexion directa a MongoAtlas
    #connectionAtlas = "mongodb+srv://WristWonders:root@wristwonderscluster.ri89dpv.mongodb.net/admin?authSource=admin&replicaSet=atlas-f0zukj-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    
    #Conexion directa a Mongo Server Locla
    connection = "mongodb://localhost:27017/"

    # client = pymongo.MongoClient(connectionAtlas)

    client = pymongo.MongoClient(connection)

    db = client["WristWondersDataBase_Dev"]
    collection = db["Usuarios"]

    print()

    resultados = collection.find()

    users = []
    for resultado in resultados:
        users.append(resultado["Nombre_Usuario"])


    print(users)
    #return users


# total_documentos = collection.count_documents({})

# print(f"Total de documentos en la colección 'productos': {total_documentos}")

# for documento in collection.find():
#     print(documento)

# for documento in collection.find_one({"Nom_Prod":"WS-1100H-2AV"}):
#     print(documento)
