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


def remove_todo(connection, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (id,))

    connection.commit()
    cursor.close()


def get_todos(connection):
    cursor = connection.cursor()
    # This will order them so that the important ones always come first,
    # and the ones that are not done will also come first
    # return cursor.execute(
    #     "SELECT * FROM todos ORDER BY important DESC, done;"
    # ).fetchall()  # it will automatically default to ASC

    todos = cursor.execute(
        "SELECT * FROM todos ORDER BY important DESC, done;"
    ).fetchall()

    cursor.close()
    return todos


def toggle_done(connection, id):
    cursor = connection.cursor()

    current_status = cursor.execute(
        "SELECT done FROM todos WHERE id = ?", (id,)
    ).fetchone()[0]
    new_status = 0 if current_status == 1 else 1

    cursor.execute(
        """UPDATE todos
           SET done = ?
           WHERE id = ?""",
        (new_status, id),
    )

    connection.commit()
    cursor.close()


def toggle_important(connection, id):
    cursor = connection.cursor()

    current_status = cursor.execute(
        "SELECT important FROM todos WHERE id = ?", (id,)
    ).fetchone()[0]
    new_status = 0 if current_status == 1 else 1

    cursor.execute(
        """UPDATE todos
           SET important = ?
           WHERE id = ?""",
        (new_status, id),
    )

    connection.commit()
    cursor.close()
