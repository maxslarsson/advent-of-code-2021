from copy import deepcopy

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def part1(temp):
    for _ in range(10):
        new = deepcopy(temp)
        for i in range(len(temp) - 1):
            z, o = temp[i], temp[i + 1]
            new.insert(2*i+1, rules[z+o])
        temp = new

    count = {}
    for elem in temp:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    count = sorted(count.items(), key=lambda x: x[1])
    return count[-1][1] - count[0][1]


if __name__ == '__main__':
    with open(INFILE) as f:
        s = f.read().split("\n")
        template = list(s[0])
        rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in s[2:]}

    print(f"Part 1: {part1(deepcopy(template))}")
