from itertools import groupby
from operator import itemgetter


def partition(order, data):
    values = {d: 0 for d in data}

    for _ in range(len(order)):
        for before, after in order:
            values[before] = values[after] - 1

    for _, part in groupby(sorted(values, key=values.get), key=values.get):
        yield list(part)


def parse_order(order_lines):
    for line in order_lines:
        left, op, right = line.split(' ')
        if op == '<':
            yield left, right
        if op == '>':
            yield right, left
