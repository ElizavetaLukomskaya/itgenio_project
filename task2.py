def minimum(mass):
    sum_row = {}
    sum_col = {}

    for i in range(len(mass)):
        rows = 0
        for j in range(len(mass[0])):
            rows += mass[i][j]
        sum_row.update({i:rows})   

    for i in range(len(mass[0])):
        cols = 0
        for j in range(len(mass)):
            cols += mass[j][i]
        sum_col.update({i:cols})   

    return [max(sum_row, key=sum_row.get), max(sum_col, key=sum_col.get)]


print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))

