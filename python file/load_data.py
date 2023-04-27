import psycopg2


def load_database(file_path, table_name):

    # To catch the exception if any
    try:

        # Connect to the postgresql server
        conn = psycopg2.connect("postgresql://dap:dap@127.0.0.1:5432/kenya_data")
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r", encoding='utf-8')
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        cur.copy_expert("copy {} from STDIN CSV HEADER".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    # Catch the exception if any
    except Exception as e:
        print("Error: {}".format(str(e)))
