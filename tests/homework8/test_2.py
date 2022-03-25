from homework8.task2 import TableData


def test_table_data():
    presidents = TableData(
        db_name='tests/homework8/example.sqlite',
        tb_name='presidents'
    )

    assert len(presidents) == 3
    assert [p['name'] for p in presidents] == [
        'Yeltsin',
        'Trump',
        'Big Man Tyrone'
    ]
    assert ('Yeltsin' in presidents) is True
    assert ('Putin' in presidents) is False
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
