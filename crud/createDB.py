import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()

    cursor.execute("create database imagecrawler")
except (Exception, psycopg2.Error) as error:
    print("Failed to create database", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
