
num_steps = 100
grid_width = 101
grid_length = 103


def get_final_coord(start_coord, velocity):
    start_coord[0] = (start_coord[0] + velocity[0]*num_steps) % grid_width
    start_coord[1] = (start_coord[1] + velocity[1]*num_steps) % grid_length

    return [start_coord[0], start_coord[1]]

end_coords = []

with open("input.txt", "r") as rf:
    while input_line := rf.readline():
        next_line = input_line.split()
        start_coord = [int(num) for num in next_line[0][2:].split(",")]
        velocity = [int(num) for num in next_line[1][2:].split(",")]
        end_coords.append(get_final_coord(start_coord, velocity))

# end_grid = [[0 for _ in range(grid_width)] for _ in range(grid_length)]

quadrant_counts = [0,0,0,0]

for coord in end_coords:
    # end_grid[coord[1]][coord[0]] += 1
    quadrant_index = 0

    if coord[0] == grid_width//2 or coord[1] == grid_length//2:
        continue

    if coord[0] > grid_width//2:
        quadrant_index += 1
    if coord[1] > grid_length//2:
        quadrant_index += 2
    quadrant_counts[quadrant_index] += 1

print(quadrant_counts)

ans = 1
for num in quadrant_counts:
    ans *= num
print(ans)