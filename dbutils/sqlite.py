from typing import Any
import sqlite3 as sqlite

from .utils import empty, PatchRowFactoryMixin


class Cursor(PatchRowFactoryMixin, sqlite.Cursor):
    def fetchall(self, row_factory=empty) -> list[Any]:
        with self._patch(row_factory):
            return super().fetchall()

    def fetchone(self, row_factory=empty) -> list[Any]:
        with self._patch(row_factory):
            return super().fetchone()

    def fetchmany(self, size: int | None = 1, row_factory=empty) -> list[Any]:
        with self._patch(row_factory):
            return super().fetchmany(size)
