import curses
import sqlite3
from curses import wrapper

import tuido.database as database

DB_PATH = "database.db"


def refresh(stdscr):
    stdscr.refresh()


def parse_todos(stdscr, connection):
    todos = database.get_todos(connection)
    y = 1

    for todo in todos:
        formatted_str = f"{'! ' if todo[1] == 1 else ''}{'X' if todo[3] == 0 else 'D'} | {todo[0]}: {todo[2]}"
        stdscr.addstr(y, 1, formatted_str)

        y += 1


def main(stdscr):
    connection = sqlite3.connect(DB_PATH)

    stdscr.clear()

    stdscr.border()

    parse_todos(stdscr, connection)

    refresh(stdscr)
    stdscr.getch()

    connection.close()


wrapper(main)
