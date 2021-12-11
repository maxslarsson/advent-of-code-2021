from copy import deepcopy

INFILE = 'input.txt'
# INFILE = 'sample.txt'


def part1(s):
    intervals = s.copy()
    for _ in range(80):
        for i in range(len(intervals)):
            if intervals[i] == 0:
                intervals[i] = 6
                intervals.append(8)
            else:
                intervals[i] -= 1
    return len(intervals)


def part2(s):
    intervals = {x: 0 for x in range(9)}
    for x in s:
        intervals[x] += 1
    for i in range(256):
        clone = intervals.copy()
        for k, v in clone.items():
            intervals[k] -= v
            if k == 0:
                intervals[6] += v
                intervals[8] += v
            else:
                intervals[k-1] += v
    return sum(intervals.values())


def main():
    with open(INFILE) as f:
        s = [int(x) for x in f.read().split(',')]

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
