import mysql.connector
from mysql.connector import Error
from main_window import main_window

def create_connection_mysql_db():
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host="localhost",  # your host, usually localhost
            port="3306",
            user="root",  # your username
            passwd="1111",  # your password
            db="air_ticket")  # name
        print("Подключение к MySQL успешно выполнено")
    except Error as db_connection_error:
        print("Возникла ошибка: ", db_connection_error)
    return connection_db

def create_new_def(conn):
    cursors = conn.cursor()
    create_db_sql_query = """show tables;"""
    cursors.execute(create_db_sql_query)
    for i in cursors.fetchall():
        print(i[0])
    conn.close()
    cursors.close()

def add_new_data(conn):
    cursors = conn.cursor()
    create_db_sql_query = f"""describe airline;"""
    cursors.execute(create_db_sql_query)
    for i in cursors.fetchall():
        print(i[0])
    conn.close()
    cursors.close()



if __name__ == '__main__':
    conn = create_connection_mysql_db()
    add_new_data(conn)
    main_window()
