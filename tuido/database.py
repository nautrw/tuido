import sqlite3


def create_table(connection):
    cursor = connection.cursor()
    # no boolean type in sqlite, so I will use
    # 1 for true and 0 for false
    cursor.execute("""CREATE TABLE IF NOT EXISTS todos
                      (id INT PRIMARY KEY, important INTEGER, task TEXT, done INTEGER)""")

    connection.commit()
    cursor.close()


def add_todo(connection, id, important, task, done):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos VALUES (?, ?, ?, ?)", (id, important, task, done))

    connection.commit()
    cursor.close()


def get_todos(connection):
    cursor = connection.cursor()
    # This will order them so that the important ones always come first,
    # and the ones that are not done will also come first
    return cursor.execute(
        "SELECT * FROM todos ORDER BY important DESC, done;"
    )  # it will automatically default to ASC
    cursor.close()
