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
    
directions = [coordinate(0, -1), coordinate(1, 0), coordinate(0, 1), coordinate(-1, 0)]

corner_directions = [
    [coordinate(-1, 0), coordinate(-1, -1), coordinate(0, -1)],
    [coordinate(0, -1), coordinate(1, -1), coordinate(1, 0)],
    [coordinate(1, 0), coordinate(1, 1), coordinate(0, 1)],
    [coordinate(0, 1), coordinate(-1, 1), coordinate(-1, 0)],
]

    
def explore(start : coordinate, grid, visited):
    queue = deque()
    queue.append(start)
    perimeter = 0
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
        
        for scan_directions in corner_directions:
            coord_1 = cur_coord.add_coord(scan_directions[0])
            coord_2 = cur_coord.add_coord(scan_directions[1]) # corner coord
            coord_3 = cur_coord.add_coord(scan_directions[2])

            if ( 
                (not coord_1.is_valid(grid) or coord_1.get_value(grid) != cur_coord.get_value(grid)) and
                (not coord_3.is_valid(grid) or coord_3.get_value(grid) != cur_coord.get_value(grid))
            ):
                perimeter += 1

            if (
                (coord_1.is_valid(grid) and coord_1.get_value(grid) == cur_coord.get_value(grid)) and
                (not coord_2.is_valid(grid) or coord_2.get_value(grid) != cur_coord.get_value(grid)) and
                (coord_3.is_valid(grid) and coord_3.get_value(grid) == cur_coord.get_value(grid))
            ):
                perimeter += 1

    return start.get_value(grid), area, perimeter, area*perimeter

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
            ans += explore(starting_coord, grid, visited)[3]

print(ans)