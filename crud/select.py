import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="testdb")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT * FROM testschema.client;")
    for record in cursor.fetchall():
        print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
