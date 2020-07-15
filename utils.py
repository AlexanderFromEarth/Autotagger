from functools import reduce


def read_file(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding) as f:
        return f.read()


def compose(funcs):
    return lambda x: reduce(lambda prev, cur: cur(prev), funcs, x)
