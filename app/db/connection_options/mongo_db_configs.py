import os

from dotenv import load_dotenv

load_dotenv()
mongo_db = {
    "MONGO_DB_USERNAME": os.environ.get("MONGO_DB_USERNAME"),
    "MONGO_DB_PASSWORD": os.environ.get("MONGO_DB_PASSWORD"),
    "MONGO_DB_HOST": os.environ.get("MONGO_DB_HOST", "localhost"),
    "MONGO_DB_PORT": os.environ.get("MONGO_DB_PORT", "27017"),
    "MONGO_DB_NAME": os.environ.get("MONGO_DB_NAME")
}