import sqlite3


class TableData:
    def __init__(self, db_name: str, tb_name: str):
        self._con = sqlite3.connect(db_name)
        self._cursor = self._con.cursor()
        self.table_name = tb_name
        self.col_names = list(
            map(
                lambda x: x[0], self._cursor.execute(
                    f"SELECT * from {self.table_name}").description
            )
        )

    def __getitem__(self, index):
        self._cursor.execute(
            'SELECT * from presidents where name=:name', {'name': 'Yeltsin'}
            # f"SELECT * from {self.table_name} WHERE name={index}"
        )
        return self._cursor.fetchone()

    def __len__(self) -> int:
        self._cursor.execute(
            f"SELECT COUNT(*) from {self.table_name}"
        )
        return self._cursor.fetchall()[0][0]

    def __iter__(self):
        self._cursor.execute(
            f"SELECT * from {self.table_name}"
        )
        while True:
            try:
                yield dict(
                    zip(self.col_names, self._cursor.fetchone())
                )
            except TypeError:  # остановка на None
                break

    def __contains__(self, item):
        for i in self.__iter__():
            if i['name'] == item:
                return True
        return False


if __name__ == '__main__':
    presidents = TableData(db_name='example.sqlite', tb_name='presidents')
    print(len(presidents))
    for p in presidents:
        print(p['name'])
    print('Yeltsin' in presidents)
    print(presidents['Yeltsin'])
