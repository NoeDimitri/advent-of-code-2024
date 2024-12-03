import re

# wow these are great lol
regex_pattern = r'mul\((\d+,\d+)\)'
ans = 0

with open("input.txt", "r") as rf:
    lines = rf.readlines()
    for line in lines:
        for command in re.findall(regex_pattern, line):
            nums = [int(num) for num in command.split(',')]
            ans += nums[0] * nums[1]
print(ans)
