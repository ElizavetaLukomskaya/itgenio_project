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


test_mass = [[0, 0, 0], [100, 200, 300], [3434, 7246, 3739], [8348327, 734676, 6]]
print(minimum(test_mass))

