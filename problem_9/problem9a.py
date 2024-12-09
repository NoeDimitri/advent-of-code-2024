import numpy

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

i = 0
end_index = len(file_queue) - 1

if file_queue[end_index].is_gap():
    end_index -= 1

while i != len(file_queue):

    if i > end_index:
        break
    
    if not file_queue[i].is_gap():
        compact.append(file_queue[i])
        i += 1
    else:
        larger_index = numpy.argmax([file_queue[i].size, file_queue[end_index].size])
        
        # automatically doesnt delete more than size
        dec_size = file_queue[end_index].decrement_size(file_queue[i].size)

        # back file wins
        if larger_index == 1:
            i += 1
        else: # gap wins
            file_queue[i].decrement_size(dec_size)
            
        compact.append(disk_file(file_queue[end_index].id, dec_size))

        if file_queue[end_index].size == 0:
            end_index -= 2


# print("".join([str(thing) for thing in compact]))
# print("0099811188827773336446555566")

ans = 0
pointer = 0
for file in compact:
    ans += file.id * sum(range(pointer, pointer+file.size))
    pointer += file.size
    
print(ans)