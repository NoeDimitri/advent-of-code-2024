import re

# wait zamb that's actually crazy
regex_pattern = r"(?:mul|don't|do)\((?:\d+,\d+)?\)"
ans = 0
active = True

with open("input.txt", "r") as rf:
    lines = rf.readlines()
    for line in lines:
        for command in re.findall(regex_pattern, line):
            if command.startswith("mul"):
                if active:
                    nums = [int(num) for num in command[4:-1].split(',')]
                    ans += nums[0] * nums[1]
            elif command.startswith("don't"):
                active = False
            elif command.startswith("do"):
                active = True

print(ans)
