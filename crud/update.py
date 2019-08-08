import psycopg2


def updateTable(mobileId, name):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="password",
                                      host="localhost",
                                      port="5432",
                                      database="testdb")

        cursor = connection.cursor()

        # Get row before update
        print("Table Before updating record ")
        sql_select_query = """select * from testschema.client where id = %s"""
        cursor.execute(sql_select_query, (mobileId, ))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """update testschema.client set name = %s where id = %s"""
        cursor.execute(sql_update_query, (name, mobileId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        # Get row after update
        print("Table After updating record ")
        sql_select_query = """select * from testschema.client where id = %s"""
        cursor.execute(sql_select_query, (mobileId, ))
        record = cursor.fetchone()
        print(record)
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


id = 3
name = "oleg"
updateTable(id, name)
