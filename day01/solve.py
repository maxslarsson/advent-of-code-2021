def part1(s):
    pass


def part2(s):
    pass


if __name__ == '__main__':
    with open('input.txt') as f:
        s = f.read()
        # or
        s = f.read().split()
        # or
        s = [int(x) for x in f.read().split()]

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")