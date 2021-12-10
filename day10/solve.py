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


def main():
    with open('input.txt') as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")


if __name__ == '__main__':
    main()
