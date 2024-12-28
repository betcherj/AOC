
data = []

with open("data.txt", "r") as f:
    raw_data = f.readlines()
    for line in raw_data:
        left, right = line.split(" ")
        left = left.split('=')[1]
        p = left.split(',')
        right = right.split("=")[1]
        v = right.split(',')
        data.append([(int(p[0]), int(p[1])), (int(v[0]), int(v[1]))])

grid_width = 101
grid_height = 103
# grid_width = 11
# grid_height = 7
seconds = 100
final_positions = []
def get_position_at_time(position, velocity, seconds, grid_width, grid_height):
    # Sim to the end and then subtract until robot is back in range?
    final_position = [position[0]+velocity[0]*seconds, position[1]+velocity[1]*seconds]
    while final_position[0] < 0:
        final_position[0] += grid_width
    while final_position[1] < 0:
        final_position[1] += grid_height
    while final_position[0] >= grid_width:
        final_position[0] -= grid_width
    while final_position[1] >= grid_height:
        final_position[1] -= grid_height
    return final_position

quadrant_one_count = 0
quadrant_two_count = 0
quadrant_three_count = 0
quadrant_four_count = 0

# Want to know where each robot will be after 100 sections
for position, velocity in data:
    final_position = get_position_at_time(position, velocity, seconds, grid_width, grid_height)
    final_positions.append(final_position)
    if final_position[0] < grid_width // 2:
        if final_position[1] < grid_height // 2:
            quadrant_one_count += 1
        elif final_position[1] > grid_height / 2:
            quadrant_two_count += 1
    elif final_position[0] > grid_width / 2:
        if final_position[1] < grid_height // 2:
            quadrant_three_count += 1
        elif final_position[1] > grid_height / 2:
            quadrant_four_count += 1
print(quadrant_one_count, quadrant_two_count, quadrant_three_count, quadrant_four_count)
print(quadrant_one_count * quadrant_two_count * quadrant_three_count * quadrant_four_count)

# visual = [['.' for i in range(grid_width)] for j in range(grid_height)]
# for final_position in final_positions:
#     if visual[final_position[1]][final_position[0]] == '.':
#         visual[final_position[1]][final_position[0]] = '1'
#     else:
#         visual[final_position[1]][final_position[0]] = str(int(visual[final_position[1]][final_position[0]]) + 1)
#
# for row in visual:
#     print(''.join(row))
















