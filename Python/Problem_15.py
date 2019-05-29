# Project Euler Problem 15

size = 20
grid = []
for i in range(size+1):
    row = []
    for j in range(size+1):
        if i == 0 or j == 0:
            row.append(1)
        else:
            row.append(row[j-1] + grid[i-1][j])
    grid.append(row)
    #print(row)

print(grid[-1][-1])
