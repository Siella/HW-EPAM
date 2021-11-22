from task_03.task_3_get_print_output import my_precious_logger


def test_stdout(capsys):
    my_precious_logger("no error")
    out, err = capsys.readouterr()
    assert out == "no error"
    assert err == ''


def test_stderr(capsys):
    my_precious_logger("error, really error")
    out, err = capsys.readouterr()
    assert out == ''
    assert err == "error, really error"


def test_empty_string(capsys):
    my_precious_logger('')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''
