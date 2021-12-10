INFILE = 'input.txt'
# INFILE = 'sample.txt'


def fuel_cost_part1(target, horizontal_positions):
    return sum(abs(pos-target) for pos in horizontal_positions)


def part1(s):
    return min(fuel_cost_part1(i, s) for i in range(min(s), max(s)+1))


def fuel_cost_part2(target, horizontal_positions):
    fuel_cost_per_crab = []
    for pos in horizontal_positions:
        n = abs(pos-target)
        s = n * (1 + n) // 2
        fuel_cost_per_crab.append(s)
    return sum(fuel_cost_per_crab)


def part2(s):
    return min(fuel_cost_part2(i, s) for i in range(min(s), max(s)+1))


def main():
    with open(INFILE) as f:
        s = [int(x) for x in f.read().split(",")]

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == '__main__':
    main()
