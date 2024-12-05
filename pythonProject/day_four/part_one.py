
with open("data.txt", "r+") as f:
    data = [[x for x in line] for line in f.readlines()]

def check_adjacent(grid, i, j, target):
    indices = []
    # top left
    if i > 0 and j > 0 and grid[i-1][j-1] == target:
        indices.append((i-1, j-1, 'tl'))
    # top
    if i > 0 and grid[i-1][j] == target:
        indices.append((i-1, j, 't'))
    # top right
    if i > 0 and j < len(data)-1 and grid[i-1][j+1] == target:
        indices.append((i-1, j+1, 'tr'))
    # right
    if j < len(data)-1 and grid[i][j+1] == target:
        indices.append((i, j+1, 'r'))
    # bottom right
    if i < len(data)-1 and j < len(data)-1 and grid[i+1][j+1] == target:
        indices.append((i+1, j+1, 'br'))
    # bottom
    if i < len(data)-1 and grid[i+1][j] == target:
        indices.append((i+1, j, 'b'))
    # bottom left
    if i < len(data)-1 and j > 0 and grid[i+1][j-1] == target:
        indices.append((i+1, j-1, 'bl'))
    # left
    if j>0 and grid[i][j-1] == target:
        indices.append((i, j-1, 'l'))

    return indices

def check_adjacent_directional(grid, i, j, direction, target):
    res = None
    # top left
    if i > 0 and j > 0 and grid[i-1][j-1] == target and direction == 'tl':
        res = (i-1, j-1)
    # top
    if i > 0 and grid[i-1][j] == target and direction == 't':
        res = (i-1, j)
    # top right
    if i > 0 and j < len(data)-1 and grid[i-1][j+1] == target and direction == 'tr':
        res = (i-1, j+1)
    # right
    if j < len(data)-1 and grid[i][j+1] == target and direction == 'r':
        res = (i, j+1)
    # bottom right
    if i < len(data)-1 and j < len(data)-1 and grid[i+1][j+1] == target and direction == 'br':
        res = (i+1, j+1)
    # bottom
    if i < len(data)-1 and grid[i+1][j] == target and direction == 'b':
        res = (i+1, j)
    # bottom left
    if i < len(data)-1 and j > 0 and grid[i+1][j-1] == target and direction == 'bl':
        res = (i+1, j-1)
    # left
    if j>0 and grid[i][j-1] == target and direction == 'l':
        res = (i, j-1)

    return res
'''
Need to find all the xmas words
- start at all the x's 
- find all the paths from all the x's to m's 
- find all the paths from m's to a's 
- find all the paths from those a's to s's 
'''

starts_x = []
paths = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            starts_x.append((i,j))

directional_starts_m = []
# Search from the X's
for i, j in starts_x:
    directional_starts_m += check_adjacent(data, i, j, 'M')

# print(starts_m)
starts_a = []
for i, j, direction in directional_starts_m:
    res = check_adjacent_directional(data, i, j, direction, 'A')
    if res:
        starts_a.append((res[0], res[1], direction))

# print(starts_a)
starts_s = []
for i, j, direction in starts_a:
    res = check_adjacent_directional(data, i, j, direction, 'S')
    if res:
        starts_s.append((res[0], res[1], direction))

print(len(starts_s))
# print(starts_s)
# print(set(starts_s))
# print(len(set(starts_s)))
# print(len(starts_s))













