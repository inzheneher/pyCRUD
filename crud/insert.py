import psycopg2
from crud.connection import Connection
from utils.config import Config

def insert():
    try:
        connection = Connection(Config()).get_connection()
        cursor = connection.cursor()
        postgres_insert_query = "insert into testschema.client (name, last_name) values (%s,%s)"
        record_to_insert = ('sidr','ivanov')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table, because: ", error)


if __name__ == '__main__':
    insert()
