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


def main():
    with open('input.txt') as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")


if __name__ == '__main__':
    main()
