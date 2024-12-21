

with open("data.txt", "r+") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]

def check_grid(data, i, j):
    # Check if we have an xmas in any orientation
    if i+2 > len(data)-1 or j+2 > len(data[0])-1:
        return False
    if data[i+1][j+1] != "A":
        return False
    corners = [data[i][j], data[i][j+2], data[i+2][j+2], data[i+2][j]]
    # We are losing too many correct cases
    if corners[0] != corners[1] and corners[0] != corners[3]:
        return False
    if corners[2] != corners[1] and corners[2] != corners[3]:
        return False
    corners.sort()
    if corners != ["M", "M", "S", "S"]:
        return False
    return True

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        count += 1 if check_grid(data, i, j) else 0

print(count)