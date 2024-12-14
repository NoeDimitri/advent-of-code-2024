from collections import deque

class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_valid(self, grid):
        if (self.x < 0 or self.x >= len(grid[0]) or self.y < 0 or self.y >= len(grid)):
                return False
        return True
    
    def turn_to_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

directions = [coordinate(0, -1), coordinate(1, 0), coordinate(0, 1), coordinate(-1, 0)]

grid = []
start_points = []

with open("input.txt", "r") as rf:
    lines = rf.readlines()
    for y in range(len(lines)):
        grid.append(lines[y].strip())
        for x in range(len(lines[y])):
            if lines[y][x] == "0":
                start_points.append(coordinate(x, y))

ans = 0

for start_point in start_points:
    queue = deque()
    finished = set()
    queue.append(start_point)
    while queue:
        cur_point = queue.popleft()

        if grid[cur_point.y][cur_point.x] == "9" and cur_point.turn_to_tuple() not in finished:
            ans += 1
            finished.add(cur_point.turn_to_tuple())

        for direction in directions:
            adjacent_point = coordinate(cur_point.x + direction.x, cur_point.y + direction.y)
            if adjacent_point.is_valid(grid) and int(grid[adjacent_point.y][adjacent_point.x]) == int(grid[cur_point.y][cur_point.x]) + 1:
                queue.append(adjacent_point)
                

print(ans)