
with open("data.txt", "r") as f:
    data = [int(x) for x in f.read()]

if len(data) / 2 != 0:
    data.append(0) # Add one free space block to the end if we need it

# First we need to uncompact the file
uncompacted_data = []
index_num = 0
for i in range(0, len(data), 2):
    uncompacted_data += [str(index_num) for i in range(data[i])]
    uncompacted_data += ['.' for i in range(data[i+1])]
    index_num += 1


data = uncompacted_data
# Then we add up the score by index and print it
i = 0
j = len(data)-1
while i < j:
    while i < len(data) and data[i] != '.':
        i+= 1
    while j > -1 and data[j] == '.':
        j -= 1
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    i += 1
    j -= 1

# Score the function
score =0
for i in range(len(data)):
    if data[i] == ".":
        break
    score += (int(data[i])*i)
print(score)
