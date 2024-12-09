import copy

class disk_file():
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def is_gap(self):
        return self.id == -1
    
    # returns amount decreased by
    def decrement_size(self, reduce_amount):
        return_amount = min(reduce_amount, self.size)
        self.size -= return_amount
        return return_amount

    def __str__(self):
        if self.is_gap():
            return "."*self.size
        return str(self.id)*self.size

input_line = ""

with open("input.txt", "r") as rf:
    input_line = rf.readline()

compact = []
file_queue = []

for i in range(len(input_line)):
    
    if i % 2 != 0:
        file_id = -1
    else:
        file_id = i//2
    
    new_file = disk_file(file_id, int(input_line[i]))

    file_queue.append(new_file)

end_index = len(file_queue) - 1

# print("".join([str(thing) for thing in file_queue]))

while end_index >= 0:
    if not file_queue[end_index].is_gap():
        for i in range(end_index):
            if file_queue[i].is_gap() and file_queue[i].size >= file_queue[end_index].size:
                file_queue[i].decrement_size(file_queue[end_index].size)
                file_queue.insert(i, disk_file(file_queue[end_index].id, file_queue[end_index].size))
                end_index += 1
                file_queue[end_index].id = -1
                break
    end_index -= 1

# print("".join([str(thing) for thing in file_queue]))
# print("00992111777.44.333....5555.6666.....8888..")

ans = 0
pointer = 0
for file in file_queue:
    if file.id != -1:
        ans += file.id * sum(range(pointer, pointer+file.size))
    pointer += file.size
    
print(ans)