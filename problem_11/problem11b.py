

with open("input.txt", "r") as rf:
    stones = [int(num) for num in rf.readline().strip().split()]

num_layers = 75

dp = {}

def solve_stone(num, layer):
    if (num, layer) in dp:
        return dp[(num, layer)]
    if layer == num_layers:
        return 1
    elif num == 0:
        temp_ans = solve_stone(1, layer+1)
    elif len(str(num)) % 2 == 0:
        first_half, second_half = int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])
        temp_ans = solve_stone(first_half, layer+1) + solve_stone(second_half, layer+1)
    else:
        temp_ans = solve_stone(num*2024, layer+1)    
    dp[(num, layer)] = temp_ans
    return temp_ans

ans = 0

for stone in stones:
    ans += solve_stone(stone, 0)

print(ans)


