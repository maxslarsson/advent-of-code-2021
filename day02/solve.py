from copy import deepcopy

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def part1(s):
    hori_pos = 0
    depth = 0
    for line in s:
        cmd, num = line.split()
        num = int(num)
        if cmd == "forward":
             hori_pos += num
        elif cmd == "up":
            depth -= num
        elif cmd == "down":
            depth += num
    return hori_pos * depth


def part2(s):
    hori_pos = 0
    depth = 0
    aim = 0
    for line in s:
        cmd, num = line.split()
        num = int(num)
        if cmd == "forward":
            hori_pos += num
            depth += aim * num
        elif cmd == "up":
            aim -= num
        elif cmd == "down":
            aim += num
    return hori_pos * depth


def main():
    with open(INFILE) as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
