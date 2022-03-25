"""
Write a function that takes directory path, a file extension
and an optional tokenizer.
It will count lines in all files with that extension
if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import glob
from pathlib import Path
from typing import Callable, Optional, Union


def universal_file_counter(
        dir_path: Union[Path, str],
        file_extension: str = 'txt',
        tokenizer: Optional[Callable] = None
) -> int:
    files = [f for f in glob.glob(f"{dir_path}/*.{file_extension}")]
    token_cnt = 0
    for file in files:
        with open(file, errors='ignore') as f:
            for line in f.readlines():
                iterable = [line] if tokenizer is None else tokenizer(line)
                token_cnt += len(iterable)
    return token_cnt


if __name__ == '__main__':
    print(universal_file_counter(Path.cwd()))
    print(universal_file_counter(Path.cwd(), tokenizer=str.split))
