from pymongo import MongoClient
# pymongo needs to be installed


def Mongo_Connect(operation, data=None):
    container_name = 'mongodb'
    client = MongoClient(f'mongodb://{container_name}:27017/')
    db = client['Goals']

    if operation == "store":
        return store(db['goal'], data)
    elif operation == "delete":
        return delete(db['goal'], data)
    else:
        return view(db['goal'])


def view(collection):
    data = []
    cursor = collection.find()
    for document in cursor:
        data.append(str(document))
    return data


def store(collection, data):
    data = view(collection)
    for values in data:
        if data['goal'].lower() in values.lower():
            return f"Goal already present: ID: {values}"
    result = collection.insert_one(data)
    return f"Inserted the data. ID: {result.inserted_id}"


def delete(collection, data):
    result = collection.find_one(data)
    if result:
        collection.delete_one(data)
        return f"Goal '{data['goal']}' deleted successfully."
    else:
        return f"Goal '{data['goal']}' not found in the collection."
