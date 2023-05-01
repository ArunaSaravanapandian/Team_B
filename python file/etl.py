from extract_data import *
from transform_data import *
from load_data import *
from visualization_data import *


def etl():
    # extract the data from the json file
    extract_database()

    # connect to the MongoDB
    client = pymongo.MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))

    # connect to the "kenya_database" and the "school_data" and "health_data" collection
    db = client['kenya_database']
    school_data_collection = db['school_data']
    health_data_collection = db['health_data']

    # store the school data returned in the variable result
    results = school_data_collection.find()

    # Data transformation for school
    school_tup = create_school(results)
    school_records = school_tup[0]
    school_headers = school_tup[1]
    create_table(school_records, school_headers, './school.csv')

    # store the health data returned in the variable result
    results = health_data_collection.find()

    # Data transformation for health
    health_tup = create_health(results)
    health_records = health_tup[0]
    health_headers = health_tup[1]
    create_table(health_records, health_headers, './health.csv')

    # load the data to the postgres
    load_database('./school.csv', 'public.school_data')
    load_database('./health.csv', 'public.health_data')

    # visualise the data
    visualize_data()


if __name__ == '__main__':
    etl()
