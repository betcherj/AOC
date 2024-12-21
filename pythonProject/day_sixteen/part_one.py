import math
from copy import deepcopy
import sys

with open('data.txt', "r") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]

# Works but is very inefficient need to implment Djkistras here

def find_paths(data, pos, visited):
    """Starting from pos return all the paths from pos to end"""
    i, j = pos
    visited[i][j] = True
    if data[i][j] == "E":
        return [[pos]]

    next_positions = []
    if i > -1 and not visited[i-1][j] and data[i-1][j] in [".", "E"]:
        next_positions.append((i-1, j))
    if j > -1 and not visited[i][j-1]  and data[i][j-1] in [".", "E"]:
        next_positions.append((i, j-1))
    if i < len(data) and not visited[i+1][j] and data[i+1][j] in [".", "E"]:
        next_positions.append((i+1, j))
    if j < len(data[0]) and not visited[i][j+1] and data[i][j+1] in [".", "E"]:
        next_positions.append((i, j+1))
    if not next_positions:
        return [] # There is no path from here
    paths = []
    for next_pos in next_positions:
        paths_from_next_pos = find_paths(data, next_pos, deepcopy(visited))
        for p in paths_from_next_pos:
            paths.append([pos] + p )
    return paths


def score_path(path):
    score = 0 # Assume move from start
    direction = "left" #Reindeer always face east first

    for i in range(1, len(path)):
        # Check if we needed to turn here or not
        last_pos = path[i-1]
        pos = path[i]
        if pos[0] == last_pos[0]:
            if pos[1] > last_pos[1]:
                next_direction = "right"
            else:
                next_direction = "left"
        else:
            if pos[0] > last_pos[0]:
                next_direction = "down"
            else:
                next_direction = "up"
        score += 1
        score += 1000 if next_direction != direction else 0
        direction = next_direction
    return score


visited = [[0 for i in range(len(data[0]))] for j in range(len(data))]

start_pos = 0
end_pos = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            start_pos = (i, j)
        if data[i][j] == "E":
            end_pos = (i, j)

paths = find_paths(data, start_pos, visited)

res = math.inf
min_path = None
for path in paths:
    path_score = score_path(path)
    if path_score < res:
        res = path_score
        min_path = path

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) in min_path:
            data[i][j] = "0"
for row in data:
    print(''.join(row))
print(res)
