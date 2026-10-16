# This CRUD module allows easy interaction with the AAC database.

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username='aacuser', password='88ww77ggWOW'): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: # check if data is present before trying to insert
            try:
                self.database.animals.insert_one(data)   
                return True
            except Exception as e:
                print("An exception occurred with insertion", e) #
                return False
        else: 
            print("Nothing to save, because data parameter is empty") 
            return False

    # Create method to implement the R in CRUD. 
    def read(self, query):
        if isinstance(query, dict) and query is not None:
            try:
                cur = self.collection.find(query)
                return list(cur)
            except Exception as e:
                print("An exception occurred", e)
                return []
        else:
            print("Query must be a dict")
            return []
        
    def update(self, query, data):
        if isinstance(query, dict) and isinstance(data, dict) and query is not None and data is not None:
            try:
                # flexibility to allow passing Mongo formatted dicts or normal data
                for x in data.keys():
                    if str(x).startswith("$"):
                        update = data
                    else:
                        update = {"$set": data}
                    update_result = self.collection.update_many(query, update)
                    updated_count = update_result.modified_count
                    return updated_count
            except Exception as e:
                print("An exception occurred", e)
                return 0
        else:
            print("Update failed due to invalid data")
            return 0
        
    def delete(self, query):
        if isinstance(query, dict) and query is not None:
            try:
                delete_result = self.collection.delete_many(query)
                deleted_count = delete_result.deleted_count
                return deleted_count
            except Exception as e:
                print("An exception occurred", e)
                return 0
        else:
            print("Delete failed due to invalid data")
            return 0
        
        