from copy import deepcopy
from functools import lru_cache
from itertools import chain

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def part1(template, rules):
    for _ in range(10):
        new = deepcopy(template)
        for i in range(len(template) - 1):
            z, o = template[i], template[i + 1]
            new.insert(2*i+1, rules[z+o])
        template = new

    count = {}
    for elem in template:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    count = sorted(count.items(), key=lambda x: x[1])
    return count[-1][1] - count[0][1]


def part2(template, rules):
    bucket = ()
    left_edge = template[0]
    right_edge = template[-1]
    for i in range(len(template) - 1):
        z, o = template[i], template[i + 1]
        bucket = add_tuples(bucket, recursive(z+o, 40, rules))

    new_bucket = {}
    for k, v in bucket:
        if k == left_edge or k == right_edge:
            new_bucket[k] = (v+1)//2
        else:
            new_bucket[k] = v//2
    sorted_bucket = sorted(new_bucket.items(), key=lambda x: x[1])
    return sorted_bucket[-1][1] - sorted_bucket[0][1]


@lru_cache(maxsize=None)
def recursive(pair, depth, rules):
    if depth == 0:
        bucket = {}
        for letter in pair:
            if letter in bucket:
                bucket[letter] += 1
            else:
                bucket[letter] = 1
        return bucket.items()
    else:
        new_pair = pair[0] + rules[pair] + pair[1]
        return add_tuples(recursive(new_pair[0:2], depth-1), recursive(new_pair[1:3], depth-1))


def add_tuples(t1, t2):
    new_dict = {}
    for k, v in chain(t1, t2):
        if k in new_dict:
            new_dict[k] += v
        else:
            new_dict[k] = v
    return new_dict.items()


def main():
    with open(INFILE) as f:
        s = f.read().split("\n")
        template = list(s[0])
        rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in s[2:]}

    print(f"Part 1: {part1(deepcopy(template), rules)}")
    print(f"Part 2: {part2(deepcopy(template), rules)}")


if __name__ == '__main__':
    main()
