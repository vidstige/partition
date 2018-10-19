import sys
from partition import parse_order, partition


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
