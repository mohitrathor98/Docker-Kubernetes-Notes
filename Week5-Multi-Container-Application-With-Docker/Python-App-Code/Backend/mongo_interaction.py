from pymongo import MongoClient
# pymongo needs to be installed


def Mongo_Connect(operation, data=None):
    container_name = 'mongodb'
    client = MongoClient(f'mongodb://mongoadmin:secret@{container_name}:27017/'
                         )
    db = client['Goals']

    if operation == "store":
        return store(db['goal'], data)
    elif operation == "delete":
        return delete(db['goal'], data)
    else:
        return view(db['goal'])


def view(collection):
    data = {'goal': []}
    cursor = collection.find()
    for document in cursor:
        data['goal'].append(document['goal'])
    return data


def store(collection, data):
    if search(collection, data):
        return f"Goal already present: {data}"
    result = collection.insert_one(data)
    return f"Inserted the data. ID: {result.inserted_id}"


def search(collection, data):
    cursor = collection.find()
    for document in cursor:
        if document['goal'].lower() == data['goal'].lower():
            return document
    return None


def delete(collection, data):
    available_record = search(collection, data)
    if available_record:
        collection.delete_one(available_record)
        return f"Goal '{data['goal']}' deleted successfully."
    else:
        return f"Goal '{data['goal']}' not found in the collection."
