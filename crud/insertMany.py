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

    postgres_insert_query = "insert into images.images " \
                            "(id, keyword, url, tags, source, original_id) " \
                            "values (%s,%s,%s,%s,%s,%s)"

    val = [
        (1, 'hey', 'hoy', 'joy', 'boy', 'moy'),
        (2, 'hey', 'hoy', 'joy', 'boy', 'moy'),
        (3, 'hey', 'hoy', 'joy', 'boy', 'moy')
    ]

    cursor.executemany(postgres_insert_query, val)
    connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into table", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
