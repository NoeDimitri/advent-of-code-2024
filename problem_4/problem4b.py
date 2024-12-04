import copy
search = "XMAS"

grid = []
ans = 0

directions = [
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]

def scan(x, y, grid):
    count_m, count_s = 0, 0
    for direction in directions:
        temp_x = x + direction[0]
        temp_y = y + direction[1]

        # to make sure we don't have SAS and MAM
        if grid[temp_y][temp_x] == grid[y - direction[1]][x - direction[0]]:
            return 0

        if grid[temp_y][temp_x] == "M":
            count_m += 1
        elif grid[temp_y][temp_x] == "S":
            count_s += 1
        else:
            return 0
    

    if count_m == 2 and count_s == 2:
        return 1


with open("input.txt", "r") as rf:
    grid = [["Z"] + [words for words in line] + ["Z"] for line in rf.read().splitlines()]
    grid.append(["Z"]*len(grid[0]))
    grid.insert(0, ["Z"]*len(grid[0]))

for y in range(len(grid)):
    for x in range(len(grid[1])):
        if grid[y][x] == 'A':
            ans += scan(x, y, grid)

print(ans)