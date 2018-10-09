import sys

def partition(order, data):
    for left, right in order:
        if right in data:
            print(left, right)
            memory = []
            while left in data:
                data.remove(left)
                memory.append(left)

            index = data.index(right)
            while memory:
                data.insert(index, memory.pop())


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
    partition(order, data)
    print(data)

if __name__ == "__main__":
    main(sys.argv[1:])
