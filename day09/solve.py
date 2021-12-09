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


def main():
    with open('input.txt') as f:
        s = [[int(num) for num in list(line)] for line in f.read().split("\n")]

    print(f"Part 1: {part1(s)}")


if __name__ == '__main__':
    main()
