from bson import ObjectId
from typing import Dict, List

class ResumesRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "resumes"
        self.__db_connection = db_connection
    
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def select_if_property_exists(self, property_name: str) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection_data = collection.find(
            {property_name: {"$exists": True}}
        )
        return [data for data in collection_data]
    
    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection_data = collection.find(
            filter,
        )
        return [data for data in collection_data]
    
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(
            filter,
        )
        return response

    def select_by_id(self, _id) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(
            {"_id": ObjectId(_id)}
        )
        return response