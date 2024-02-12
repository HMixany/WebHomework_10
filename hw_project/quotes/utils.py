from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://userweb17:<password>@cluster0.r7yz0bl.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
def get_mongodb():
    client = MongoClient(uri)
    db = client.WHW_8
    return db