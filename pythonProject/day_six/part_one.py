

def sim_guard_path(data, guard_position, direction):
    visited = [[0 for i in range(len(line))] for line in data]
    while guard_position[0] < len(data) and guard_position[0] > -1 and guard_position[1] < len(data[0]) and guard_position[1] > -1:
        visited[guard_position[0]][guard_position[1]] = 1

        next_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        if next_position[0] < len(data) and next_position[0] > -1 and next_position[1] < len(data[0]) and next_position[1] > -1 and data[next_position[0]][next_position[1]] == "#":
            #Rotate the direction to the right
            if direction == (-1, 0):
                direction = (0, 1)
            elif direction == (0,1):
                direction = (1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, -1):
                direction = (-1, 0)
            else:
                raise Exception("SHOULD NOT HAVE GOT HERE")
        else:
            guard_position = next_position

    return visited

with open("data.txt", "r") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]

guard_position = None
direction = None

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            direction = (-1, 0)
            guard_position = (i, j)

        if data[i][j] == ">":
            direction = (0,1)
            guard_position = (i, j)


        if data[i][j] == "v":
            direction = (1,0)
            guard_position = (i, j)

        if data[i][j] == "<":
            direction = (0,-1)
            guard_position = (i, j)


visited = sim_guard_path(data, guard_position, direction)
print(sum([sum(line) for line in visited]))
