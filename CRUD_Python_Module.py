from pymongo import MongoClient
from pymongo.errors import PyMongoError

class CRUD:
    def __init__(self, username, password):
        try:
            # Connection to MongoDB
            self.client = MongoClient(
                f"mongodb://{username}:{password}@localhost:27017/?authSource=admin"
            )
            self.database = self.client['aac']
            self.collection = self.database['animals']
        except PyMongoError as e:
            print("Connection failed:", e)

    # CREATE
    def create(self, data):
        """
        Inserts a document into the collection
        :param data: dictionary
        :return: True if successful, False otherwise
        """
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            else:
                return False
        except PyMongoError as e:
            print("Insert failed:", e)
            return False

    # READ
    def read(self, query):
        """
        Queries documents from the collection
        :param query: dictionary
        :return: list of documents or empty list
        """
        try:
            if query is not None:
                cursor = self.collection.find(query)
                return list(cursor)
            else:
                return []
        except PyMongoError as e:
            print("Read failed:", e)
            return []
        
    #UPDATE
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print("Update failed:", e)
            return 0
    
    #DELETE
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete failed:", e)
            return 0