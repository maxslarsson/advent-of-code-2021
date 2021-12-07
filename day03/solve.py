def part1(s):
    most_common = ""
    least_common = ""
    for i in range(len(s[0])):
        bits = [l[i] for l in s]
        z = bits.count('0')
        o = bits.count('1')
        most_common += str(int(o > z))
        least_common += str(int(o < z))
    gamma = int(most_common, 2)
    epsilon = int(least_common, 2)
    return gamma * epsilon


def part2(s):
    oxy = s.copy()
    i = 0
    while len(oxy) > 1:
        bits = [l[i] for l in oxy]
        z = bits.count('0')
        o = bits.count('1')
        most_common = "1" if o == z else str(int(o > z))
        oxy = list(filter(lambda l: l[i] == most_common, oxy))
        i += 1

    co2 = s.copy()
    i = 0
    while len(co2) > 1:
        bits = [l[i] for l in co2]
        z = bits.count('0')
        o = bits.count('1')
        least_common = "0" if o == z else str(int(o < z))
        co2 = list(filter(lambda l: l[i] == least_common, co2))
        i += 1

    return int(oxy[0], 2) * int(co2[0], 2)


def main():
    with open('input.txt') as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == '__main__':
    main()
