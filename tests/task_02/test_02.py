from unittest.mock import patch

import pytest

from task_02.task_2_mock_input import count_dots_on_i


# Some stupid test
@patch("urllib.request.urlopen")
def test_count_i(mock_urlopen):
    mock_urlopen.return_value.__enter__.return_value.\
        read.return_value.decode.return_value = 'Hi'
    assert count_dots_on_i('') == 1


def test_proper_url():
    assert count_dots_on_i("https://example.com/") == 59


@patch("urllib.request.urlopen")
def test_bad_connection(mock_urlopen):
    mock_urlopen.side_effect = ConnectionError
    with pytest.raises(ValueError) as excinfo:
        count_dots_on_i("https://example.com/")
    assert "Unreachable https://example.com/" in str(excinfo.value)
