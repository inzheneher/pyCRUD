import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="imagecrawler",
    )

    cursor = connection.cursor()

    cursor.execute("create table images.images ("
                   "id varchar(255) primary key,"
                   "keyword varchar(32),"
                   "url varchar(255),"
                   "tags varchar(255),"
                   "source varchar(64),"
                   "original_id varchar(64))")

    connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to create schema", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
