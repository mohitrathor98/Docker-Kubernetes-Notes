from pymongo import MongoClient
# pymongo needs to be installed


def Mongo_Connect(operation, data=None):
    client = MongoClient('mongodb://172.17.0.2:27017/')
    db = client['Goals']

    if operation == "store":
        return "store"
    elif operation == "delete":
        return "delete"
    else:
        return view(db['goal'])


def view(collection):
    data = []
    cursor = collection.find()
    for document in cursor:
        data.append(document)
    return data
