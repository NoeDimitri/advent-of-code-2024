

with open("input.txt", "r") as rf:
    stones = [int(num) for num in rf.readline().strip().split()]

num_layers = 25

def solve_stone(num, layer):
    if layer == num_layers:
        # print(num, end=" ")
        return 1
    elif num == 0:
         return solve_stone(1, layer+1)
    elif len(str(num)) % 2 == 0:
        first_half, second_half = int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])
        return solve_stone(first_half, layer+1) + solve_stone(second_half, layer+1)
    else:
        return solve_stone(num*2024, layer+1)

ans = 0

for stone in stones:
    ans += solve_stone(stone, 0)

print()
print(ans)


