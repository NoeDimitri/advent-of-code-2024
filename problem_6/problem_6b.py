grid = []
cur_coord = (-1,-1) # x, y
# up right down left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_index = 0
traveled = set()

def valid_coord(coord, grid):
    if coord[0] < 0 or coord[0] >= len(grid[0]) or coord[1] < 0 or coord[1] >= len(grid):
        return False
    return True


def check_looping(coord, dir_index, grid, obstacle_spot):

    visited = {}

    while True:
        if dir_index in visited.get(coord, set()):
            grid[obstacle_spot[1]][obstacle_spot[0]] = "O"
            return True

        # mark we've been here
        temp_set = visited.get(coord, set())
        temp_set.add(dir_index)
        visited[coord] = temp_set

        # find next coordinate
        next_pos = (coord[0] + directions[dir_index][0], coord[1] + directions[dir_index][1])

        # are we out of bounds
        if not valid_coord(next_pos, grid):
            return False
        
        # if we bump into an object, rotate to right
        while grid[next_pos[1]][next_pos[0]] == "#" or next_pos == obstacle_spot:
            dir_index = (dir_index + 1) % len(directions)
            next_pos = (coord[0] + directions[dir_index][0], coord[1] + directions[dir_index][1])
            # edge case if obstacle on boundary
            if not valid_coord(next_pos, grid):
                return False
        
        coord = next_pos

with open("input.txt", "r") as rf:
    for line in rf.readlines():
        grid.append([thing for thing in line.strip()])
        if "^" in grid[-1]:
            for i in range(len(grid[-1])):
                if grid[-1][i] == "^":
                    start = (i, len(grid)-1)
                    cur_coord = start

ans = 0
while True:
    traveled.add(cur_coord)
    next_pos = (cur_coord[0] + directions[dir_index][0], cur_coord[1] + directions[dir_index][1])

    # check if we exited
    if not valid_coord(next_pos, grid):
        break

    # oh we hit an object lol
    while grid[next_pos[1]][next_pos[0]] == "#":
        dir_index = (dir_index + 1) % len(directions)
        next_pos = (cur_coord[0] + directions[dir_index][0], cur_coord[1] + directions[dir_index][1])
        if not valid_coord(next_pos, grid):
            break

    # pretend next tile is an obstacle
    # exclusive to part 6
    if grid[next_pos[1]][next_pos[0]] == "." and next_pos not in traveled and check_looping(cur_coord, (dir_index + 1) % len(directions), grid, next_pos):
        ans += 1

    cur_coord = next_pos

with open("output.txt", "w") as wf:
    for line in grid:
        wf.write("".join(line))
        wf.write("\n")

print(ans)