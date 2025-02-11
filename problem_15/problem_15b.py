instruction_map = {
    "^" : [0, -1],
    ">" : [1, 0],
    "v" : [0, 1],
    "<" : [-1, 0]
}

opposite_char = {
    "[" : "]",
    "]" : "["
}

grid = []
instructions = ""
# x, y
cur_pos = []

with open("input.txt", "r") as rf:
    i = 0
    while (next_line := [char for char in rf.readline().strip()]) != []:        
        line_augmented = []
        for item in next_line:
            if item == "#":
                line_augmented += ["#", "#"]
            if item == "O":
                line_augmented += ["[", "]"]
            if item == ".":
                line_augmented += [".", "."]
            if item == "@":
                line_augmented += ["@", "."]
        grid.append(line_augmented)

        if '@' in line_augmented:
            cur_pos = [line_augmented.index('@'), i]
        i += 1
    while (next_line := rf.readline().strip()):
        instructions += next_line

def move(cur_coord, direction, grid):
    next_coord = [cur_coord[0] + direction[0], cur_coord[1] + direction[1]]

    # don't move
    if grid[next_coord[1]][next_coord[0]] == "#":
        return cur_coord
    
    # move normally
    if grid[next_coord[1]][next_coord[0]] == ".":
        grid[next_coord[1]][next_coord[0]] = "@"
        grid[cur_coord[1]][cur_coord[0]] = "."
        return next_coord
    
    # we pusha da box
    next_coord = [cur_coord[0] + direction[0], cur_coord[1] + direction[1]]

    if direction == [1,0] or direction == [-1, 0]:
        if push_horizontal(next_coord, direction, grid, "@"):
            grid[cur_coord[1]][cur_coord[0]] = "."
            return next_coord
    elif direction == [0, 1] or direction == [0, -1]:
        if push_vertical(next_coord, direction, grid):
            grid[cur_coord[1]][cur_coord[0]] = "."
            return next_coord
        
    return cur_coord

# doing this one recursively
def push_horizontal(cur_coord, direction, grid, prev_char):
    cur_char = grid[cur_coord[1]][cur_coord[0]]

    if grid[cur_coord[1]][cur_coord[0]] == "#":
        return False
    if grid[cur_coord[1]][cur_coord[0]] == ".":
        grid[cur_coord[1]][cur_coord[0]] = prev_char
        return True
    
    if(return_val := push_horizontal([cur_coord[0] + direction[0], cur_coord[1] + direction[1]], direction, grid, cur_char)):
        grid[cur_coord[1]][cur_coord[0]] = prev_char

    return return_val # true or false

# doing this one iteratively because if one fails then we do nothing 
def push_vertical(start_coord, direction, grid):

    queue = [(start_coord, "@")]
    visited = set()
    updates = []

    while queue:
        cur_pair = queue.pop(0)
        cur_coord = cur_pair[0]
        
        if tuple(cur_coord) in visited:
            continue

        visited.add(tuple(cur_coord))
        
        cur_char = grid[cur_coord[1]][cur_coord[0]]

        if cur_char == "#":
            return False
        
        updates.append(cur_pair)

        if cur_char == "[":
            # spot to the right
            queue.append(([cur_coord[0] + 1, cur_coord[1]], "."))
            queue.append(([cur_coord[0], cur_coord[1] + direction[1]], cur_char))
        elif cur_char == "]":
            queue.append(([cur_coord[0] - 1, cur_coord[1]], "."))
            queue.append(([cur_coord[0], cur_coord[1] + direction[1]], cur_char))

    for update in updates:
        coord = update[0]
        grid[coord[1]][coord[0]] = update[1]

    return True

i = 1
for instruction in instructions:
    cur_pos = move(cur_pos, instruction_map[instruction], grid)

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "[":
            ans += y * 100 + x

print(ans)