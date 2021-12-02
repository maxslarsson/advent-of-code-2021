def part1(s):
    hori_pos = 0
    depth = 0
    for c in s:
        cmd, num = c.split()
        if cmd == "forward":
             hori_pos += int(num)
        elif cmd == "up":
            depth -= int(num)
        elif cmd == "down":
            depth += int(num)
    return hori_pos * depth


def part2(s):
    hori_pos = 0
    depth = 0
    aim = 0
    for c in s:
        cmd, num = c.split()
        if cmd == "forward":
            hori_pos += int(num)
            depth += aim * int(num)
        elif cmd == "up":
            aim -= int(num)
        elif cmd == "down":
            aim += int(num)
    return hori_pos * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")