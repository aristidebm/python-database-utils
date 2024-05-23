### What is dbutils ?

**dbutils** offers some helpers to increase DX when working with databases in python.

**dbutils**  can be helpful in case you have requirements below:

+ You don't want to install an orm for whatever reasons.
+ You still need goodies offered by an orm, you know accessing database columns as python object fields.
+ You are ready to fork the project and fix it in case something doesn't work.

### Example

```python
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
```

Running the code above will output something like this

```bash
[Person(username='user_135730002995607', password='1234'),
 Person(username='user_135730002997661', password='1234'),
 Person(username='user_135730002998222', password='1234'),
 Person(username='user_135730002998562', password='1234'),
 Person(username='user_135730002998843', password='1234'),
 Person(username='user_135730002999213', password='1234'),
 Person(username='user_135730002999464', password='1234'),
 Person(username='user_135730002999694', password='1234'),
 Person(username='user_135730002999945', password='1234'),
 Person(username='user_135730003000185', password='1234')]
```
