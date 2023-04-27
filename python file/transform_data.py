def create_school(results):
    # Takes the query outcome and convert to a list and return it.
    records = []
    headers = ['OBJECTID', 'SCHOOL_NAM', 'County', 'X_Coord', 'Y_Coord']
    for record in results:
        object_id = str(record['OBJECTID'])
        school_name = str(record['SCHOOL_NAM'])
        county = str(record['County'])
        latitude = str(record['X_Coord'])
        longitude = str(record['Y_Coord'])
        tmp = [object_id, school_name, county, latitude, longitude]
        records.append(tmp)
    print('School table created')
    return records, headers


def create_health(results):
    # Takes the query outcome and convert to a list and return it.
    records = []
    headers = ['OBJECTID', 'FACILITY_N', 'county', 'Latitude', 'Longitude']   
    for record in results:
        object_id = str(record['OBJECTID'])
        facility_name = str(record['Facility_N'])
        county = str(record['County'])
        latitude = str(record['Latitude'])
        longitude = str(record['Longitude'])
        tmp = [object_id, facility_name, county, latitude, longitude]
        records.append(tmp)
    return records, headers


def create_table(records, headers, file_path):
    # Take a list of records and headers and generate csv
    f = open(file_path, 'w', encoding='utf-8')
    row_len = len(headers)
    f.write(format_list(headers, row_len, ',', '"'))
    for record in records:
        f.write(format_list(record, row_len, ',', '"'))
    f.close()
    print('CSV file successfully created: {}'.format(file_path))


def format_list(list, length, delimiter, quote):
    # format the list
    counter = 1
    string = ''
    for record in list:
        if counter == length:
            string += quote + record + quote + '\n'
        else:
            string += quote + record + quote + delimiter
        counter += 1
    return string
