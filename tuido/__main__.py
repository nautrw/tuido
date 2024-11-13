import sqlite3

import tuido.database as database

DB_PATH = "database.db"


def main():
    connection = sqlite3.connect(DB_PATH)

    database.create_table(connection)
    database.add_todo(connection, 8289, 0, "not important done", 1)
    database.add_todo(connection, 9292, 1, "important done", 1)
    database.add_todo(connection, 7222, 0, "not important not done", 0)
    database.add_todo(connection, 7371, 1, "important not done", 0)

    todos_list = database.get_todos(connection)
    for todo in todos_list:
        print(todo)

    connection.close()


main()
