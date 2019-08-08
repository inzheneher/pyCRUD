import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="testdb")
    cursor = connection.cursor()
    postgres_insert_query = """insert into testschema.client (name, last_name) values (%s,%s)"""
    record_to_insert = ('igor','kirillov')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
