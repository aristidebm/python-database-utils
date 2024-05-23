import time
from pprint import pprint
import sqlite3 as sqlite
from dataclasses import dataclass
from dbutils import SQLiteCursor, class_row


@dataclass
class Person:
    username: str
    password: str


def main():
    with sqlite.connect(":memory:") as conn:
        cur = conn.cursor(SQLiteCursor)
        cur.execute(
            "create table if not exists persons (username varchar unique, password varchar);"
        )
        cur.executemany(
            "insert into persons (username, password) values (:username, :password);",
            [
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
                {"username": f"user_{time.monotonic_ns()}", "password": "1234"},
            ],
        )
        res = cur.execute("select * from persons;")
        pprint(res.fetchall(row_factory=class_row(Person)))


if __name__ == "__main__":
    main()
