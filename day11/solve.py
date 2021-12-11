from copy import deepcopy

INFILE = 'input.txt'
# INFILE = 'sample1.txt'
# INFILE = 'sample2.txt'


def part1(s):
    total_flashes = 0
    for _ in range(100):
        for row in range(len(s)):
            for col in range(len(s[0])):
                s[row][col] += 1

        flashed = [[False for _ in range(len(s[0]))] for _ in range(len(s))]
        for row in range(len(s)):
            for col in range(len(s[0])):
                flash(row, col, s, flashed)
        total_flashes += sum(sum(row) for row in flashed)

        for row in range(len(s)):
            for col in range(len(s[0])):
                if flashed[row][col]:
                    s[row][col] = 0

    return total_flashes


def part2(s):
    steps = 0
    while True:
        steps += 1

        for row in range(len(s)):
            for col in range(len(s[0])):
                s[row][col] += 1

        flashed = [[False for _ in range(len(s[0]))] for _ in range(len(s))]
        for row in range(len(s)):
            for col in range(len(s[0])):
                flash(row, col, s, flashed)

        if sum(sum(row) for row in flashed) == len(s[0]) * len(s):
            return steps

        for row in range(len(s)):
            for col in range(len(s[0])):
                if flashed[row][col]:
                    s[row][col] = 0


# NOTE: An octopus can only flash at most once per step.
def flash(row, col, grid, flashed):
    if grid[row][col] > 9 and not flashed[row][col]:
        flashed[row][col] = True
        drow = [0, 0, 1, 1, 1, -1, -1, -1]
        dcol = [1, -1, 1, -1, 0, 1, -1, 0]
        for row_d, col_d in zip(drow, dcol):
            if 0 <= row + row_d < len(grid) and 0 <= col + col_d < len(grid[0]):
                grid[row + row_d][col + col_d] += 1
                flash(row + row_d, col + col_d, grid, flashed)


def main():
    with open(INFILE) as f:
        s = [[int(c) for c in line] for line in f.read().split("\n")]

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
