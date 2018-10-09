import sys

def main(order, input_files):
    print(order, input_files)


if __name__ == "__main__":
    args = sys.argv[1:]
    order_file = args.pop(0)
    with open(order_file) as f:
        order = [line.strip() for line in f if line.strip()]
    data = []
    for path in args:
        with open(path) as f:
            data.extend([line.strip() for line in f if line.strip()])
    main(order, data)
