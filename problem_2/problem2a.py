
ans = 0

with open("input.txt", "r") as rf:
    while line := rf.readline():
        level = [int(num) for num in line.split()]
        diffs = list(map(lambda x, y: y - x, level[:-1], level[1:]))

        # I love confusing if statements

        if all((abs(num) > 0 and abs(num) <= 3) for num in diffs) and len(set(num < 0 for num in  diffs)) == 1:
            ans += 1


print(ans)