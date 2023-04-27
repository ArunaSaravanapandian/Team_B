import json
import pymongo
from io import UnsupportedOperation


def extract_database():
    # try block for the exception
    try:

        # connecting to the mongodb
        client = pymongo.MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))
        print("Connecting to the MongoDB")

        # creating a new database "kenya_database" to store the value from the .json files
        db = client['kenya_database']

        # creating a collection "school_data_collection" to store data corresponding to school
        school_data_collection = db['school_data']

        # creating a collection "health_data_collection" to store data corresponding to health
        health_data_collection = db['health_data']

        # Get the data from .json file and loading it in school_json
        with open(r'schools.json', 'r') as data_school:
            school_json = json.load(data_school)

        # Get the data from .json file and loading it in health_json
        with open(r'healthcare_facilities.json', 'r') as data_health:
            health_json = json.load(data_health)

        # Insert the data into the school_data_collection
        for i in school_json['features']:
            if i["properties"] is not None:
                school_data_collection.insert_one(i["properties"])
            else:
                continue

        # Insert the data into the health_data_collection
        for i in health_json['features']:
            if i["properties"] is not None:
                health_data_collection.insert_one(i["properties"])
            else:
                continue

    # handling the exception if it has occurred
    except UnsupportedOperation as e:
        print("Error: {}".format(str(e)))

    print("Extraction complete")
    