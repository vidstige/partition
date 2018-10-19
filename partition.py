import sys
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


def _slurp(path):
     with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def main(args):
    order_file = args.pop(0)
    order = list(parse_order(_slurp(order_file)))

    data = []
    for path in args:
        data.extend(_slurp(path))

    for part in partition(order, data):
        print(part)

if __name__ == "__main__":
    main(sys.argv[1:])
