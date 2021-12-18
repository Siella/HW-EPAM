import sqlite3


class ValidationError(Exception):
    pass


class DataBaseConnectionError(Exception):
    pass


def connect(f):
    def with_connection(self, *args, **kwargs):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            result = f(self, cursor, *args, **kwargs)
        except ConnectionError:
            raise DataBaseConnectionError('Cannot connect to db!')
        finally:
            conn.close()
        return result
    return with_connection


class TableData:
    """
    Враппер для таблицы БД.

    :param db_name: путь до БД
    :type db_name: str
    :param tb_name: название таблицы в БД
    :type tb_name: str
    """

    def __init__(self, db_name: str, tb_name: str):
        self.db_name = db_name
        if not tb_name.isalnum():
            raise ValidationError('Table name is invalid!')
        self.table_name = tb_name
        self._index = 1

    @connect
    def __getitem__(self, cursor, index):
        cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE name=:name',
            {'name': index}
        )
        return cursor.fetchone()

    @connect
    def __len__(self, cursor) -> int:
        cursor.execute(
            f'SELECT COUNT(*) FROM {self.table_name}'
        )
        return cursor.fetchall()[0][0]

    @connect
    def __iter__(self, cursor):
        self._cols = list(
            map(lambda x: x[0], cursor.execute(
                f'SELECT * FROM {self.table_name}').description)
        )
        return self

    @connect
    def __next__(self, cursor):
        if self._index < self.__len__() + 1:
            cursor.execute(
                f'SELECT * FROM {self.table_name} WHERE rowid=:rowid',
                {'rowid': self._index}
            )
            self._index += 1
            return dict(zip(self._cols, cursor.fetchone()))
        else:
            raise StopIteration

    @connect
    def __contains__(self, cursor, item):
        if self.__getitem__(item):
            return True
        return False


if __name__ == '__main__':
    presidents = TableData(db_name='example.sqlite', tb_name='presidents')
    print(len(presidents))
    for p in presidents:
        print(p['name'])
    print('Yeltsin' in presidents)
    print(presidents['Yeltsin'])
