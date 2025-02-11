
num_steps = 100
grid_width = 101
grid_length = 103
num_iter = 10000


coords = []

with open("input.txt", "r") as rf:
    while input_line := rf.readline():
        next_line = input_line.split()
        start_coord = [int(num) for num in next_line[0][2:].split(",")]
        velocity = [int(num) for num in next_line[1][2:].split(",")]
        coords.append([start_coord, velocity])

with open("output.txt", "w") as wf:
    for i in range(1,num_iter):
        end_grid = [[0 for _ in range(grid_width)] for _ in range(grid_length)]
        for coord_pair in coords:
            coord_pair[0][0] =  (coord_pair[0][0] + coord_pair[1][0]) % grid_width
            coord_pair[0][1] =  (coord_pair[0][1] + coord_pair[1][1]) % grid_length
            end_grid[coord_pair[0][1]][coord_pair[0][0]] += 1
        wf.write(f"{i}\n")
        for line in end_grid:
            wf.write("".join(["#" if num != 0 else "." for num in line]) + "\n")