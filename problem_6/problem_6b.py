grid = []
cur_coord = (-1,-1) # x, y
# up right down left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_index = 0

def valid_coord(coord, grid):
    if coord[0] < 0 or coord[0] >= len(grid[0]) or coord[1] < 0 or coord[1] >= len(grid):
        return False
    return True

def increment_coord(coord, direction):
    return (coord[0] + directions[direction][0], coord[1] + directions[direction][1])

def check_looping(coord, dir_index, grid, obstacle_spot):

    fast = [coord, dir_index, 2]
    slow = [coord, dir_index, 1]

    while True:
        for traveler in [fast, slow]:
            for _ in range(traveler[2]):
                next_pos = increment_coord(traveler[0], traveler[1])
                
                if not valid_coord(next_pos, grid):
                    return False
                
                while grid[next_pos[1]][next_pos[0]] == "#" or next_pos == obstacle_spot:

                    traveler[1] = (traveler[1] + 1) % len(directions)
                    next_pos = increment_coord(traveler[0], traveler[1])

                    if not valid_coord(next_pos, grid):
                        return False

                traveler[0] = next_pos

                if fast[0] == slow[0] and fast[1] == slow[1]:
                    grid[obstacle_spot[1]][obstacle_spot[0]] = "O"
                    return True

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
    next_pos = increment_coord(cur_coord, dir_index)

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
    if grid[next_pos[1]][next_pos[0]] == "." and check_looping(cur_coord, (dir_index + 1) % len(directions), grid, next_pos):
        ans += 1

    cur_coord = next_pos

with open("output.txt", "w") as wf:
    for line in grid:
        wf.write("".join(line))
        wf.write("\n")

print(ans)