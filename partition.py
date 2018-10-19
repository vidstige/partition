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


def main(args):
    order_file = args.pop(0)
    with open(order_file) as f:
        raw_order = [line.strip() for line in f if line.strip()]
        order = list(parse_order(raw_order))

    data = []
    for path in args:
        with open(path) as f:
            data.extend([line.strip() for line in f if line.strip()])

    for part in partition(order, data):
        print(part)

if __name__ == "__main__":
    main(sys.argv[1:])
