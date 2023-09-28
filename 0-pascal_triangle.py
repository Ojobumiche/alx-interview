#This returns a list of lists of integers representing the Pascal’s triangle of n.
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] if i == 0 else [1, 1]
        if i > 1:
            for j in range(1, i):
                previous_row = triangle[i - 1]
                row.insert(j, previous_row[j - 1] + previous_row[j])
        triangle.append(row)

    return triangle
