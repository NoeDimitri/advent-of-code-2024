ordering = []
updates = []

with open("input.txt", "r") as rf:
    while (line:= rf.readline()) != "\n":
        ordering.append(line.strip())
    while (line:= rf.readline()):
        updates.append(line.strip())

order_dict = {}

for line in ordering:
    before, after = line.split("|")
    order_dict[before] = order_dict.get(before, []) + [after]

ans = 0

# I'll be honest I didn't expect this to work lol
for update in updates:
    after_count = {}
    pages = update.split(",")
    valid = True
    for page in pages:
        for page2 in pages:
            if page in order_dict and page2 in order_dict[page]:
                after_count[page] = after_count.get(page, 0) + 1

    correct_order = [0]*len(pages)

    for page in pages:
        correct_order[len(pages) - after_count.get(page, 0) - 1] = page
    
    if correct_order != pages:
        ans += int(correct_order[len(pages)//2])

print(ans)