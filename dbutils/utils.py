from contextlib import contextmanager

__all__ = ["class_row", "empty", "PatchRowFactoryMixin"]


def class_row(klass):
    def row_factory(cursor, row):
        fields = [_get_field(column) for column in cursor.description]
        data = dict(zip(fields, row))
        return klass(**data)

    def _get_field(column):
        if isinstance(column, (list, tuple)):
            return column[0]
        return column.name

    return row_factory


class empty:
    ...


class PatchRowFactoryMixin:
    @contextmanager
    def _patch(self, row_factory=empty):
        old = self.row_factory

        if self.row_factory is not empty:
            self.row_factory = row_factory

        yield self

        self.row_factory = old
