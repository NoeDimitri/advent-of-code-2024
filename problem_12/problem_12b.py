from collections import deque

class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_valid(self, grid):
        if (self.x < 0 or self.x >= len(grid[0]) or self.y < 0 or self.y >= len(grid)):
                return False
        return True
    
    def get_value(self, grid):
        return grid[self.y][self.x]
    
    def add_coord(self, new_coord):
        return coordinate(self.x + new_coord.x, self.y + new_coord.y)
    
    def turn_to_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
directions = [coordinate(-1, 0), coordinate(0, -1), coordinate(1, 0), coordinate(0, 1)]
#left, up, right, down
    
def explore(start : coordinate, grid, visited):
    queue = deque()
    queue.append(start)
    area = 0

    while queue:
        cur_coord = queue.popleft()

        if cur_coord.turn_to_tuple() in visited:
            continue

        area += 1
        visited.add(cur_coord.turn_to_tuple())

        for direction in directions:
            possible_coord = cur_coord.add_coord(direction)
            
            # if this next coord is part of our cluster
            if (possible_coord.is_valid(grid) and 
                possible_coord.get_value(grid) == cur_coord.get_value(grid)):
                    if possible_coord.turn_to_tuple() not in visited:
                        queue.append(possible_coord)

    return start.get_value(grid), area

def find_num_sides(start_coord: coordinate, grid):
    dir_index = 2 # start facing right
    num_sides = 1 # assume we counted top-most wall already

    cur_coord = start_coord

    right_coord, down_coord = start_coord.add_coord(directions[2]), start_coord.add_coord(directions[3])

    if (right_coord.is_valid(grid) and right_coord.get_value(grid) == right_coord.get_value(grid)):
        dir_index = 2
        cur_coord = right_coord
    elif (down_coord.is_valid(grid) and down_coord.get_value(grid) == down_coord.get_value(grid)):
        dir_index = 3
        cur_coord = down_coord
    else:
        # all sides not valid, must be just one block
        return 4
    
    while cur_coord.turn_to_tuple() != start_coord.turn_to_tuple():
        temp_coord = cur_coord.add_coord(directions[dir_index])
        while (not temp_coord.is_valid(grid) or 
            temp_coord.get_value(grid) != temp_coord.get_value(grid)):
                dir_index = (dir_index + 1) % len(directions)
                num_sides += 1
                temp_coord = cur_coord.add_coord(directions[dir_index])
        cur_coord = temp_coord
                
    return start_coord.get_value(grid), num_sides
    

grid = []

with open("input.txt", "r") as rf:
    for line in rf.readlines():
        grid.append([letter for letter in line.strip()])

visited = set()

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) not  in visited:
            starting_coord = coordinate(x, y)
            ans += explore(starting_coord, grid, visited)[1]
            print(find_num_sides(starting_coord, grid))

# print(ans)