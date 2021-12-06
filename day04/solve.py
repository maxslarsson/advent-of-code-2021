class Board:
    def __init__(self, b):
        self.board = [[(num, False) for num in row] for row in b]

    def mark(self, n):
        for row in self.board:
            for i, num in enumerate(row):
                if num[0] == n:
                    row[i] = (num[0], True)

    # Check if there is bingo on the board
    def bingo(self):
        for row in self.board:
            if all(num[1] for num in row):
                return True

        for col in range(len(self.board[0])):
            if all(self.board[i][col][1] for i in range(len(self.board))):
                return True

        return False

    def sum_of_unmarked(self):
        return sum(num[0] for row in self.board for num in row if not num[1])


def part1(nums, boards):
    for num in nums:
        for board in boards:
            board.mark(num)
            if board.bingo():
                return board.sum_of_unmarked()*num


def part2(nums, boards):
    for num in nums:
        for board in boards:
            board.mark(num)
        if len(boards) == 1 and boards[0].bingo():
            return boards[0].sum_of_unmarked() * num
        boards = [board for board in boards if not board.bingo()]


def create_boards(s):
    boards = []
    prev_empty_row = 2
    for i, e in enumerate(s + ['']):
        if e == '':
            board = s[prev_empty_row:i]
            board = [[int(num) for num in row.split()] for row in board]
            boards.append(Board(board))
            prev_empty_row = i + 1
    return boards


def main():
    with open('input.txt') as f:
        s = f.read().split("\n")

    nums = [int(num) for num in s[0].split(',')]
    boards = create_boards(s[2:])

    print(f"Part 1: {part1(nums, boards)}")
    print(f"Part 2: {part2(nums, boards)}")


if __name__ == '__main__':
    main()
