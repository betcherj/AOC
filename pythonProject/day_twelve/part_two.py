
with open("data.txt", "r") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]



def get_region(x, y, target_value, data, visited):
    stack = [(x, y)]
    fencing = 0
    total_visited = 0
    while stack:
        i, j = stack.pop()
        if visited[i][j]:
            continue
        visited[i][j] = 1
        total_visited += 1
        if i - 1 > -1:
            if data[i - 1][j] == target_value and not visited[i - 1][j]:
                stack.append((i - 1, j))
            if data[i - 1][j] != target_value:
                fencing += 1
        else:
            fencing += 1 # We are out of bounds

        if i + 1 < len(data):
            if data[i + 1][j] == target_value and not visited[i + 1][j]:
                stack.append((i + 1, j))
            if data[i + 1][j] != target_value:
                fencing += 1
        else:
            fencing += 1  # We are out of bounds

        if j - 1 > -1:
            if data[i][j-1] == target_value and not visited[i][j-1]:
                stack.append((i, j-1))
            if data[i][j-1] != target_value:
                fencing += 1
        else:
            fencing += 1 # We are out of bounds

        if j + 1 < len(data):
            if data[i][j+1] == target_value and not visited[i][j+1]:
                stack.append((i, j+1))
            if data[i][j+1] != target_value:
                fencing += 1
        else:
            fencing += 1  # We are out of bounds
    return fencing, visited, total_visited

# For each distinct group, we count the amount of fence posts
visited = [[0 for x in range(len(data[0]))] for y in range(len(data))]
total_fencing = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if not visited[i][j]:
            # Count region
            target = data[i][j]
            region_fencing, visited, num_visited = get_region(i, j, target, data, visited)
            print(region_fencing)
            for row in visited:
                print(row)
            total_fencing += region_fencing*num_visited
print(total_fencing)
