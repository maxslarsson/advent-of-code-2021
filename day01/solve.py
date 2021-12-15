from copy import deepcopy

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def part1(s):
    num_times_increased = 0

    for i in range(len(s)-1):
        if s[i+1] - s[i] > 0:
            num_times_increased += 1

    return num_times_increased


def part2(s):
    num_times_increased = 0

    for i in range(len(s)-3):
        first_window = s[i]
        # first_window = sum([s[i], s[i+1], s[i+2]])
        second_window = s[i+3]
        # second_window = sum([s[i+1], s[i+2], s[i+3]])
        if second_window-first_window > 0:
            num_times_increased += 1

    return num_times_increased


def main():
    with open(INFILE) as f:
        s = [int(x) for x in f.read().split()]

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
