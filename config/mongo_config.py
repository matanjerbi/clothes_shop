from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "api_data"

COLLECTION_USERS_NAME = "sales"
COLLECTION_SHIPPING_NAME = "shipping"


client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

collection_users = db[COLLECTION_USERS_NAME]
collection_shipping = db[COLLECTION_SHIPPING_NAME]
