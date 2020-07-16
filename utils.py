from math import ceil
from functools import reduce
from itertools import islice


def read_file(path, encoding='utf-8'):
    with open(path, 'r', encoding=encoding) as f:
        return f.read()


def compose(funcs):
    return lambda x: reduce(lambda prev, cur: cur(prev), funcs, x)


def columnize(sequence, cols=2):
    size = ceil(len(sequence) / cols)
    slices = [
        islice(sequence, pos, pos + size)
        for pos in range(0, len(sequence), size)
    ]
    return zip(*slices)
