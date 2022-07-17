from typing import Iterator, List, Any
import re


def build_query(cmd: str, value: str, file: Iterator) -> List[Any]:
    if cmd == 'filter':
        res = list(filter(lambda data: value in data, file))
        return res

    if cmd == 'map':
        res = list(map(lambda data: data.split(' ')[int(value)], file))
        return res

    if cmd == 'unique':
        res = list(set(file))
        return res

    if cmd == 'sort':
        reverse = value == 'desc'
        res = list(sorted(file, reverse=reverse))
        return res

    if cmd == 'limit':
        list_file = list(file)
        res = list_file[:int(value)]
        return res

    if cmd == 'regex':
        regex = re.compile(value)
        res = list(filter(lambda data: regex.search(data), file))
        return res

    return []
