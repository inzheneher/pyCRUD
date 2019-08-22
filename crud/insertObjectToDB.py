import psycopg2


class MyClass:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def __getitem__(self, item):
        return self._item[item]


try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="testdb")
    cursor = connection.cursor()
    postgres_insert_query = "insert into " \
                            "testschema.client (name, last_name) " \
                            "values (%s,%s) " \
                            "on conflict do nothing"
    record_to_insert = ('sidr','ivanov')
    tuple_of_records = [
        ('sidr1','ivanov4'),
        ('sidr2','ivanov3'),
        ('sidr3','ivanov2'),
        ('sidr4','ivanov1')
    ]

    person1 = MyClass('Ivan', 'Ivanov')
    person2 = MyClass('Petr', 'Petrov')

    cursor.execute(postgres_insert_query, person1)

    # cursor.executemany(postgres_insert_query, tuple_of_records)
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
