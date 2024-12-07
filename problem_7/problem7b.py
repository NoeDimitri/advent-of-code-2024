import math
import copy

ans = 0

with open("input.txt", "r") as rf:
    for line in rf.readlines():
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = [int(num) for num in numbers.split()]
        possible_solutions = [numbers.pop(0)]
        next_solutions = []

        while numbers:
            next_num = numbers.pop(0)
            for prev_num in possible_solutions:
                next_solutions.append(prev_num+next_num)
                next_solutions.append(prev_num*next_num)
                next_solutions.append(int(str(prev_num)+str(next_num)))

            possible_solutions = copy.copy(next_solutions)
            next_solutions = []

        if test_value in possible_solutions:
            ans += test_value
    
print(ans)