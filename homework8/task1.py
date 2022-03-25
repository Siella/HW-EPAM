import re
from collections import defaultdict


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class AssignValueError(ValueError):
    pass


class KeyValueStorage:
    """
    Контекстный менеджер для работы с парами key-value,
    полученных из файла.

    :param file_path: путь до файла
    :type file_path: str
    :param sep: разделитель пар
    :type sep: str
    :param storage: хранилище пар key-value
    :type storage: defaultdict
    """
    def __init__(self, file_path: str, sep: str):
        self.file_path = file_path
        self.sep = sep
        self.storage = defaultdict(str)

    def __enter__(self):
        self.file_obj = open(self.file_path, "r+")
        self._parse_file()
        return self.storage

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

    def _parse_file(self):
        """
        Парсер текстового файла с обработкой разных ситуаций,
        например, невозможность объявления/присвоения переменной
        1=something.
        """
        text = self.file_obj.read()
        items = [i for i in text.split(self.sep) if i]
        for item in items:
            pair = KeyValuePair(*item.split('='))

            key_pattern = re.compile('^[a-zA-Z_$][a-zA-Z_$0-9]*$')
            if not key_pattern.match(pair.key):
                raise AssignValueError(
                    'Value cannot be assigned to an attribute!'
                )

            self.storage[pair.key] = pair.value

            val_pattern_num = re.compile('[0-9]+$')
            if val_pattern_num.match(pair.value):
                self.storage[pair.key] = float(pair.value)


if __name__ == '__main__':
    storage = KeyValueStorage('task1.txt', '\n')
    with storage as s:
        print(s['name'])
