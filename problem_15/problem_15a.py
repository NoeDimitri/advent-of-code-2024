instruction_map = {
    "^" : [0, -1],
    ">" : [1, 0],
    "v" : [0, 1],
    "<" : [-1, 0]
}

grid = []
instructions = ""
# x, y
cur_pos = []

with open("input.txt", "r") as rf:
    grid.append([char for char in rf.readline().strip()])
    i = 1
    while (next_line := [char for char in rf.readline().strip()]) != []:        
        grid.append(next_line)
        if '@' in next_line:
            cur_pos = [next_line.index('@'), i]
        i += 1
    while (next_line := rf.readline().strip()):
        instructions += next_line

def move(cur_coord, direction, grid):
    next_coord = [cur_coord[0] + direction[0], cur_coord[1] + direction[1]]
    if grid[next_coord[1]][next_coord[0]] == "#":
        return cur_coord
    if grid[next_coord[1]][next_coord[0]] == ".":
        grid[next_coord[1]][next_coord[0]] = "@"
        grid[cur_coord[1]][cur_coord[0]] = "."
        return next_coord
    
    # we have a box
    runner_coord = [cur_coord[0] + direction[0], cur_coord[1] + direction[1]]

    while grid[runner_coord[1]][runner_coord[0]] == "O":
        runner_coord = [runner_coord[0] + direction[0], runner_coord[1] + direction[1]]

    if grid[runner_coord[1]][runner_coord[0]] == ".":
        grid[runner_coord[1]][runner_coord[0]] = "O"
        grid[next_coord[1]][next_coord[0]] = "@"
        grid[cur_coord[1]][cur_coord[0]] = "."
        return next_coord
    
    return cur_coord

for instruction in instructions:
    cur_pos = move(cur_pos, instruction_map[instruction], grid)

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            ans += y * 100 + x

print(ans)