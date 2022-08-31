import os
from typing import List, Tuple, Any


def find_deep(path: str) -> List[str] | Tuple[Any, ...]:
    """
    Find files that start with the word deep in their title.
    :param path: root to directory that contain files.
    :return: list of files.
    """
    try:
        file = os.listdir(path)
        return [name for name in file if str(name).startswith("deep")]
    except FileNotFoundError as e:
        return e.args


if __name__ == '__main__':
    print(find_deep('C:\\Users\\USER\\gitHub\\Notebooks1\\week05\\images'))
