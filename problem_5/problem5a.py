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
    order_dict[after] = order_dict.get(after, []) + [before]

ans = 0

for update in updates:
    invalid_nums = set()
    pages = update.split(",")
    valid = True
    for page in pages:
        if page in invalid_nums:
            valid = False
            break
        for invalid_pages in order_dict.get(page, []):
            invalid_nums.add(invalid_pages)
    if valid:
        ans += int(pages[len(pages)//2])

print(ans)