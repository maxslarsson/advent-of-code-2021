from copy import deepcopy
from itertools import permutations

INFILE = 'input.txt'
# INFILE = 'sample1.txt'
# INFILE = 'sample2.txt'


def part1(s):
    uniq_length_to_num = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    running_total = 0
    for line in s:
        signal_patterns, output = line.split(" | ")
        signal_patterns = signal_patterns.split(" ")
        output = output.split(" ")
        for comb in output:
            if len(comb) in uniq_length_to_num:
                running_total += 1
    return running_total


def part2(s):
    alphabet = list("abcdefg")
    mapping = {
        0: list("abcefg"),
        1: list("cf"),
        2: list("acdeg"),
        3: list("acdfg"),
        4: list("bcdf"),
        5: list("abdfg"),
        6: list("abdefg"),
        7: list("acf"),
        8: list("abcdefg"),
        9: list("abcdfg")
    }
    running_total = 0
    for line in s:
        signal_patterns, outputs = line.split(" | ")
        signal_patterns = [set(x) for x in signal_patterns.split(" ")]
        outputs = outputs.split(" ")

        for subset in permutations(alphabet):
            subset = list(subset)
            for i in range(10):
                combination = [subset[alphabet.index(letter)] for letter in mapping[i]]
                if set(combination) not in signal_patterns:
                    break
            else:
                break

        value = ""
        for output_value in outputs:
            decoded = {alphabet[subset.index(letter)] for letter in output_value}
            for num, letters in mapping.items():
                if decoded == set(letters):
                    value += str(num)
                    break

        running_total += int(value)

    return running_total


def main():
    with open(INFILE) as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(deepcopy(s))}")
    print(f"Part 2: {part2(deepcopy(s))}")


if __name__ == '__main__':
    main()
