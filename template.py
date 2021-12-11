from copy import deepcopy

# INFILE = 'input.txt'
INFILE = 'sample.txt'


def part1(s):
    pass


def part2(s):
    pass


def main():
    with open(INFILE) as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
