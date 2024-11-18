points = [(1, 2), (3, 4), (5, 6)]

def transform_point(point):
    x, y = point
    return (x, y + 10)

updated_points = list(map(transform_point , points))

print(updated_points)