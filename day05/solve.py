INFILE = 'input.txt'
# INFILE = 'sample.txt'


class Equation:
    def __init__(self, point1, point2, slope_numerator, slope_denominator):
        self.point = point1
        self.left_x, self.right_x = min(point1[0], point2[0]), max(point1[0], point2[0])
        self.bottom_y, self.top_y = min(point1[1], point2[1]), max(point1[1], point2[1])
        self.slope_numerator = slope_numerator
        self.slope_denominator = slope_denominator

    def is_point_on_line(self, point):
        if point[0] < self.left_x or point[0] > self.right_x:
            return False
        elif point[1] < self.bottom_y or point[1] > self.top_y:
            return False
        else:
            if self.slope_numerator == 0:
                return point[1] == self.point[1]
            elif self.slope_denominator == 0:
                return point[0] == self.point[0]
            else:
                x = point[0]
                y = point[1]
                slope = self.slope_numerator / self.slope_denominator
                return y - self.point[1] == slope * (x - self.point[0])


def part1(s):
    equations = []
    for l in s:
        point1, point2 = l.split(" -> ")
        x1, y1 = [int(x) for x in point1.split(",")]
        x2, y2 = [int(x) for x in point2.split(",")]

        if x1 != x2 and y1 != y2:
            continue

        slope_numerator = int(y2) - int(y1)
        slope_denominator = int(x2) - int(x1)
        equations.append(Equation((x1, y1), (x2, y2), slope_numerator, slope_denominator))

    find_num_points_with_more_than_two_lines_intersecting(equations)


def part2(s):
    equations = []
    for l in s:
        point1, point2 = l.split(" -> ")
        x1, y1 = [int(x) for x in point1.split(",")]
        x2, y2 = [int(x) for x in point2.split(",")]

        slope_numerator = int(y2) - int(y1)
        slope_denominator = int(x2) - int(x1)
        equations.append(Equation((x1, y1), (x2, y2), slope_numerator, slope_denominator))

    find_num_points_with_more_than_two_lines_intersecting(equations)


def find_num_points_with_more_than_two_lines_intersecting(equations):
    max_x, min_x = max(eq.top_y for eq in equations), min(eq.bottom_y for eq in equations)
    max_y, min_y = max(eq.right_x for eq in equations), min(eq.left_x for eq in equations)

    at_least_two_lines_overlap = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            intersections = 0
            for eq in equations:
                if eq.is_point_on_line((x, y)):
                    intersections += 1

            if intersections >= 2:
                at_least_two_lines_overlap += 1
    return at_least_two_lines_overlap


def main():
    with open(INFILE) as f:
        s = f.read().split("\n")

    print(f"Part 1: {part1(s)}")
    print(f"Part 2: {part2(s)}")


if __name__ == '__main__':
    main()
