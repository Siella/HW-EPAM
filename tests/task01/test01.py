from task01.task01 import f, cache_dict


def test_f_caching(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    for i in range(4):
        f()
        print(cache_dict)
    assert f() not in cache_dict
