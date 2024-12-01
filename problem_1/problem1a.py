
arr1 = []
arr2 = []

with open("input.txt", "r") as rf:
    while line := rf.readline():
        num1, num2 = line.split()
        arr1.append(int(num1))
        arr2.append(int(num2))

arr1.sort()
arr2.sort()

ans = 0

for pair in zip(arr1, arr2):
    ans += abs(pair[0] - pair[1])

print(ans)