points = [(1, 2), (3, 4), (-1, 5), (6, -3)]


def distance(point):
    num1, num2 = point[0], point[1]
    return (num1 ** 2 + num2 ** 2) ** 0.5

sorted_points = sorted(points, key=distance)

print(sorted_points)
