import mysql.connector

def query_database(query):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="bcg_db"
    )

    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()
    connection.close()

    return result