ans = 0

def solve_level(level):
    diffs = list(map(lambda x, y: y - x, level[:-1], level[1:]))
    if all((abs(num) > 0 and abs(num) <= 3) for num in diffs) and len(set(num < 0 for num in  diffs)) == 1:
        return True
    
with open("input.txt", "r") as rf:
    while line := rf.readline():
        level = [int(num) for num in line.split()]

        if solve_level(level):
            ans += 1
        else:
            for i in range(len(level)):
                new_level = level[0:i] + level[i+1:]
                if solve_level(new_level):
                    ans += 1
                    break


print(ans)