import sqlite3

import tuido.database as database

DB_PATH = "database.db"


def main():
    connection = sqlite3.connect(DB_PATH)

    database.create_table(connection)
    database.add_todo(connection, "test")
    database.add_todo(connection, "test2", 1)
    database.add_todo(connection, "test3", 0)

    todos_list = database.get_todos(connection)
    for todo in todos_list:
        print(todo)

    connection.close()


main()
