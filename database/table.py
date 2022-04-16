import sqlite3


def createTable():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS days (
                                    day TEXT PRIMARY KEY,
                                    full_day TEXT 
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insert(day, full_day):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()


        insert_data_query = '''INSERT INTO days (day, full_day)
                               VALUES (?, ?);'''
        cursor.execute(insert_data_query, (day, full_day,))
        sqlite_connection.commit()
        print("Запись успешно добавлена.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectTableBooks():
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite")

        sqlite_select_query = "SELECT * FROM days;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def selectName(day):
    try:
        sqlite_connection = sqlite3.connect("sqlite_pyth.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена SQLite")

        sqlite_select_query = "SELECT * FROM days WHERE day = ?"
        cursor.execute(sqlite_select_query, (day,))
        records = cursor.fetchone()
        return records[1]

    except sqlite3.Error as error:
        print("При работе с бызой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

