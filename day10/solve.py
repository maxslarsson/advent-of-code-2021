opposite = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}


def part1(s):
    first_invalid_chars = []

    for line in s:
        stack = []
        for c in line:
            if c in opposite.keys():
                stack.append(c)
            elif c == opposite[stack[-1]]:
                stack.pop()
            else:
                first_invalid_chars.append(c)
                break
    lookup_table = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return sum(lookup_table[c] for c in first_invalid_chars)


def part2(s):
    missing_closing_characters = []
    for line in s:
        stack = []
        for c in line:
            if c in opposite.keys():
                stack.append(c)
            elif c == opposite[stack[-1]]:
                stack.pop()
            else:
                break
        else:
            missing_closing_characters.append(reversed([opposite[c] for c in stack]))

    lookup_table = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    total_scores = []
    for line in missing_closing_characters:
        total_score = 0
        for c in line:
            total_score *= 5
            total_score += lookup_table[c]
        total_scores.append(total_score)
    total_scores = sorted(total_scores)
    return total_scores[len(total_scores)//2]


def main():
    with open('input.txt') as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == '__main__':
    main()
