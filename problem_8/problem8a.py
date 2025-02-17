def valid_coord(coord, cur_char, grid):
    if (coord[0] < 0 or coord[0] >= len(grid[0]) or coord[1] < 0 or coord[1] >= len(grid)):
            return False
    if grid[coord[1]][coord[0]] != cur_char:
        return True

def calculate_distance(coord1, coord2):
    y = coord2[1] - coord1[1]
    x = coord2[0] - coord1[0]
    return (x, y)

def add_coord(coord, distance):
    y = coord[1] - distance[1]
    x = coord[0] - distance[0]
    return (x, y)

grid = []
frequencies = {}
with open("input.txt", "r") as rf:
    y = 0
    for line in rf.readlines():
        cur_line = [thing for thing in line.strip()]
        for x in range(len(cur_line)):
            if cur_line[x] != ".":
                freq_array = frequencies.get(cur_line[x], [])
                freq_array.append((x, y))
                frequencies[cur_line[x]] = freq_array
        grid.append(cur_line)
        y += 1



antinodes = set()

for key in frequencies:
    coordinates = frequencies[key]
    for i in range(len(coordinates)):
        coord1 = coordinates[i]
        for j in range(i+1, len(coordinates)):
            coord2 = coordinates[j]
            diff1, diff2 = calculate_distance(coord1, coord2), calculate_distance(coord2, coord1)
            possible_antinodes = set()
            
            for start_coord in [coord1, coord2]:
                for diff in [diff1, diff2]:
                    possible_antinodes.add(add_coord(start_coord, diff))

            for anti in possible_antinodes:
                if valid_coord(anti, key, grid):
                    antinodes.add(anti)
                    if grid[anti[1]][anti[0]] == ".":
                        grid[anti[1]][anti[0]] = "#"

# for line in grid:
#     print(line)

print(len(antinodes))