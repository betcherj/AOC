with open("data.txt", "r+") as f:
    data = [[x for x in line] for line in f.readlines()]


def check_grid(data, i, j):
    # Check if we have an xmas in any orientation
    if i+2>len(data)-1 or j +  2 > len(data[0])-1:
        return False
    if data[i+1][j+1] != "A":
        return False
    corners = [data[i-1, j-1], data[i+1][j+1], data[i-1][j+1], data[i+1][j+1]]
    pass