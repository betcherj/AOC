
with open("data.txt", "r") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]

def count_region(i, j, target_value, data, visited):
    neighbors = []
    visited[i][j] = 1
    # Move to the neighbor cells
    if i - 1 > 0 and data[i-1][j] == target_value and not visited[i-1][j]:
        neighbors.append((i-1, j))
    if j - 1 > 0 and data[i][j-1] == target_value and not visited[i][j-1]:
        neighbors.append((i, j-1))
    if i + 1 < len(data) - 1 and data[i+1][j] == target_value and not visited[i+1][j]:
        neighbors.append((i+1, j))
    if j + 1 < len(data[0]) - 1 and data[i][j+1] == target_value and not visited[i][j+1]:
        neighbors.append((i, j+1))
    perimeter  = 4 - len(neighbors)
    area = 1
    for x, y in neighbors:
        neighbor_area, neighbor_perimeter, visited = count_region(x, y, target_value, data, visited)
        perimeter += neighbor_perimeter
        area += neighbor_area
    return area, perimeter,  visited


# For each distinct group, we count the amount of fence posts
visited = [[0 for x in range(len(data[0]))] for y in range(len(data))]
total_fencing = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if not visited[i][j]:
            # Count region
            target = data[i][j]
            region_area, region_perimeter,  visited= count_region(i, j, target, data, visited)
            total_fencing += (region_area * region_perimeter)
            print(visited)

print(total_fencing)


