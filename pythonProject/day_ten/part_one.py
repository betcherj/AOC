
with open("data.txt", "r") as f:
    data = [[int(x) for x in line.strip()] for line in f.readlines()]

def trail_head_score(data, x, y, visited):
    if data[x][y] == 9 and (x, y) not in visited:
        visited[(x, y)] = 1
        return 1

    next_pos = []
    for i in [-1, 1]:
        if i+x < len(data) and i+x > -1 and data[i+x][y] == data[x][y] + 1:
            next_pos.append((i+x, y))

        if i+y < len(data[0]) and i+y > -1 and data[x][i+y]  == data[x][y] + 1:
            next_pos.append((x, i+y))

    return sum([trail_head_score(data, a, b, visited) for a, b in next_pos])


# Find all the starting positions
starting_positions = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            starting_positions.append((i,j))

# Score each position and return the sum
res = 0
for position in starting_positions:
    score = trail_head_score(data, position[0], position[1], {})
    res += score

print(res)
