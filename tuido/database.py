import sqlite3


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS todos
                      (task TEXT, done INTEGER)""")  # since there is no boolean datatype in sqlite3, use 1 for done and 0 for not done

    connection.commit()


def add_todo(connection, task, done=0):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos VALUES (?, ?)", (task, done))

    connection.commit()


def get_todos(connection):
    cursor = connection.cursor()
    # `ORDER BY done ASC` orders the todos from not done to done
    return cursor.execute("SELECT task, done FROM todos ORDER BY done ASC")
