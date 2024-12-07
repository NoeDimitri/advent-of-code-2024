def valid_coord(coord, grid):
    if coord[0] < 0 or coord[0] >= len(grid[0]) or coord[1] < 0 or coord[1] >= len(grid):
        return False
    return True

grid = []
cur_coord = (-1,-1) # x, y

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_index = 0

with open("input.txt", "r") as rf:
    for line in rf.readlines():
        grid.append([thing for thing in line.strip()])
        if "^" in grid[-1]:
            for i in range(len(grid[-1])):
                if grid[-1][i] == "^":
                    cur_coord = (i, len(grid)-1)

#uhh find a better condition lol
while True:
    grid[cur_coord[1]][cur_coord[0]] = "X"

    next_pos = (cur_coord[0] + directions[dir_index][0], cur_coord[1] + directions[dir_index][1])

    # check if we exited
    if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
        break

    # oh we hit an object lol
    while grid[next_pos[1]][next_pos[0]] == "#":
        dir_index = (dir_index + 1) % len(directions)
        next_pos = (cur_coord[0] + directions[dir_index][0], cur_coord[1] + directions[dir_index][1])

    cur_coord = next_pos

# I LOVE DIFFICULT TO READ LIST COMPREHENSIONS !!!!
ans = sum([sum([1 for thing in row if thing == "X"]) for row in grid])

print(ans)