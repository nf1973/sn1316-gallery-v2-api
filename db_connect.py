from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# Prerequisite: Cluster must have
# - a db called "photo_gallery"
# - containing a collection called "galleries"


def connect_galleries():

    load_dotenv(find_dotenv())
    user = os.environ.get("MONGODB_USER")
    password = os.environ.get("MONGODB_PWD")
    cluster = os.environ.get("MONGODB_CLUSTER")

    connection_string = f"mongodb+srv://{user}:{password}@{cluster}"
    client = MongoClient(connection_string)

    pg = client.photo_gallery
    return (pg.galleries)
