from pymongo import MongoClient

from .mongo_db_configs import mongo_db

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            mongo_db["MONGO_DB_USERNAME"],
            mongo_db["MONGO_DB_PASSWORD"],
            mongo_db["MONGO_DB_HOST"],
            mongo_db["MONGO_DB_PORT"],
        )
        self.__db_name = mongo_db["MONGO_DB_NAME"]
        self.__client = None,
        self.__db_connection = None
        
    def connection_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__db_name]
    
    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__db_client
    
    def close_connection(self):
        if self.__client:
            self.__client.close()
            self.__client = None
            self.__db_connection = None
            print("[DEBUG] Database connection closed.")
        else:
            print("[DEBUG] No active database connection to close.")