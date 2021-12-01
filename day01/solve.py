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


if __name__ == '__main__':
    with open('input.txt') as f:
        s = f.read()

    # s = """199
    # 200
    # 208
    # 210
    # 200
    # 207
    # 240
    # 269
    # 260
    # 263"""

    s = [int(x) for x in s.split()]

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")