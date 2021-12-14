import re
from collections import defaultdict


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class AssignValueError(ValueError):
    pass


class KeyValueStorage:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.storage = defaultdict(str)

    def __enter__(self):
        self.file_obj = open(self.file_path, "r+")
        self._parse_file()
        return self.storage

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

    def _parse_file(self):
        for line in self.file_obj:
            pair = KeyValuePair(*line.split('='))

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
    storage = KeyValueStorage('task1.txt')
    with storage as s:
        print(s['name'])
