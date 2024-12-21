import copy
from random import gauss


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

def is_loop(data, guard_position, direction):
    visited = [[[False, None] for i in range(len(line))] for line in data]
    iterations = 0
    while guard_position[0] < len(data) and guard_position[0] > -1 and guard_position[1] < len(data[0]) and guard_position[1] > -1:
        iterations += 1
        if iterations > 100000:
            print("FOUND THE ISSUE INDEX")
            print(guard_position, direction)

            print("VISITED")
            # for item in visited:
            #     print(item)
            # print("DATA")
            # for item in data:
            #     print(item)
            raise Exception("Problem")

        if visited[guard_position[0]][guard_position[1]][0] and direction == visited[guard_position[0]][guard_position[1]][1]:
            print("Found Loop")
            return True

        visited[guard_position[0]][guard_position[1]] = [1, direction]

        next_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        if next_position[0] < len(data) and next_position[0] > -1 and next_position[1] < len(data[0]) and next_position[1] > -1 and data[next_position[0]][next_position[1]] == "#":
            # Rotate the direction to the right
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

    return False


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


# Need to record direction with visited
original_visited = sim_guard_path(data, guard_position, direction)
print("original_path")
res = 0
# Try to add a blocker to every position where the guard has been
for i in range(len(original_visited)):
    for j in range(len(original_visited[0])):
        if original_visited[i][j] == 1 and guard_position != (i,j):
            data_copy = copy.deepcopy(data)
            data_copy[i][j] = "#"
            # print("iteration")
            # print(i, j)
            # print(guard_position)
            if is_loop(data_copy, guard_position, direction):
                res += 1
    print(direction, guard_position)

    print("second loop of visited")
print(res)