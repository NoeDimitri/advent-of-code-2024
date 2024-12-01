from collections import Counter

arr1 = []
arr2 = []

with open("input.txt", "r") as rf:
    while line := rf.readline():
        num1, num2 = line.split()
        arr1.append(int(num1))
        arr2.append(int(num2))

freq_map = Counter(arr2)

ans = 0

for num in arr1:
    ans += num*freq_map.get(num, 0)

print(ans)