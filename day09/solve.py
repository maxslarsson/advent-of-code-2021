from copy import deepcopy

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def part1(s):
    low_points = []

    for i in range(len(s)):
        for j in range(len(s[0])):
            adjacent_values = []
            for i_off, j_off in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                row = i + i_off
                col = j + j_off
                if 0 <= row < len(s) and 0 <= col < len(s[0]):
                    adjacent_values.append(s[row][col])

            if all(s[i][j] < v for v in adjacent_values):
                low_points.append(s[i][j])

    return sum(p + 1 for p in low_points)


def part2(s):
    basins_to_members = {}

    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 9:
                continue

            if any((i, j) in l for l in basins_to_members.values()):
                continue

            recursive(s, (i, j), basins_to_members)

    basins_to_members = sorted(basins_to_members.values(), key=lambda item: len(item), reverse=True)
    return len(basins_to_members[0]) * len(basins_to_members[1]) * len(basins_to_members[2])


def recursive(grid, pos, basins_to_members, members=None):
    if members is None:
        members = set()

    adj_pos = set()
    for i_off, j_off in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        row = pos[0] + i_off
        col = pos[1] + j_off
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] != 9:
                adj_pos.add((row, col))

    members |= adj_pos

    if all(grid[pos[0]][pos[1]] < grid[v[0]][v[1]] for v in adj_pos):
        try:
            basins_to_members[pos] |= members
        except KeyError:
            basins_to_members[pos] = members
    else:
        min_pos = pos
        for p in adj_pos:
            if grid[p[0]][p[1]] < grid[min_pos[0]][min_pos[1]]:
                min_pos = p
        recursive(grid, min_pos, basins_to_members, members)


def main():
    with open(INFILE) as f:
        s = [[int(num) for num in list(line)] for line in f.read().split("\n")]

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
