import pytest

from homework8.task1 import KeyValueStorage


def test_normal_case():
    with KeyValueStorage(
            'tests/homework8/test1_task1.txt', '\n'
    ) as storage:
        assert storage['name'] == 'kek'
        assert storage['last_name'] == 'top'
        assert storage['power_999_abc'] == 9001
        assert storage['song'] == 'shadilay'


def test_invalid_assignment():
    with pytest.raises(Exception) as excinfo:
        with KeyValueStorage(
                'tests/homework8/test2_task1.txt', '\n'
        ) as storage:
            print(storage)
    assert str(excinfo.value) == 'Value cannot be assigned to an attribute!'
