import copy
search = "XMAS"

grid = []
ans = 0

#oh crap you can go diagonal
directions = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]

# MANNN LOSING MY MIND I didnt fully read THE PROBLEMM
def bfs(x, y, grid):
    queue = []
    # word progress, coordinate, visited
    queue.append((grid[y][x], (x, y), set()))
    count = 0

    while queue:
        next_node = queue.pop()
        visited = next_node[2].copy()
        visited.add(next_node[1])

        if next_node[0] == search:
            print(next_node)
            count += 1
            continue

        if not search.startswith(next_node[0]):
            continue
        
        for direction in directions:
            x1, y1 = next_node[1]
            next_coords = (x1 + direction[0], y1 + direction[1])
            if next_coords not in visited:
                next_word = next_node[0] + grid[next_coords[1]][next_coords[0]]
                queue.append((next_word, next_coords, visited))

    return count

def scan(x, y, grid, direction):
    word = "X"
    while search.startswith(word):
        if word == search:
            return 1
        x += direction[0]
        y += direction[1]
        word += grid[y][x]
    return 0

with open("input.txt", "r") as rf:
    grid = [["Z"] + [words for words in line] + ["Z"] for line in rf.read().splitlines()]
    grid.append(["Z"]*len(grid[0]))
    grid.insert(0, ["Z"]*len(grid[0]))

for y in range(len(grid)):
    for x in range(len(grid[1])):
        if grid[y][x] == 'X':
            for direction in directions:
                ans += scan(x, y, grid, direction)

print(ans)