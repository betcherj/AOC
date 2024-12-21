from fractions import Fraction

def mark_anti_nodes(locations, anti_nodes):
    for i in range(len(locations)):
        x_1, y_1 = locations[i]
        for j in range(i+1, len(locations)):
            x_2, y_2 = locations[j]
            horizontal = abs(x_1-x_2)
            vertical = abs(y_1-y_2)
            vertical = Fraction(vertical/horizontal).numerator
            horizontal = Fraction(vertical/horizontal).denominator
            print(vertical, horizontal)
            an1_x = x_1
            an2_x = x_1
            an1_y = y_1
            an2_y = y_1
            multiplier = 1
            while (an1_y > -1 and an1_y < len(data) and an1_x > -1 and an1_x < len(data)) or (an2_y > -1 and an2_y < len(data) and an2_x > -1 and an2_x < len(data)):
                if x_1 < x_2:
                    an1_x = x_1 - vertical * multiplier
                    an2_x = x_2 + horizontal * multiplier
                else:
                    an1_x = x_1 + horizontal * multiplier
                    an2_x = x_1 - horizontal * multiplier

                if y_1 < y_2:
                    an1_y = y_1 - vertical * multiplier
                    an2_y = y_2 + vertical * multiplier
                else:
                    an1_y = y_1 + vertical * multiplier
                    an2_y = y_2 - vertical * multiplier

                # Now we check if these are in the bounds and add them to our list
                if an1_y > -1 and an1_y < len(data) and an1_x > -1 and an1_x < len(data):
                    anti_nodes[an1_y][an1_x] = 1
                if an2_y > -1 and an2_y < len(data) and an2_x > -1 and an2_x < len(data):
                    anti_nodes[an2_y][an2_x] = 1
                multiplier += 1


    return anti_nodes


with open("data.txt", "r") as f:
    data = [[x for x in line.strip()] for line in f.readlines()]


anti_nodes = [[0 for x in range(len(line))] for line in data]
antenna_locations = {}
# Create a map of all the locations of the antenna
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != ".":
            if data[i][j] in antenna_locations:
                antenna_locations[data[i][j]] += [(i,j)]
            else:
                antenna_locations[data[i][j]] = [(i,j)]

# For each unique frequency plot the lines between them and add the antinodes
for key, value in antenna_locations.items():
    anti_nodes = mark_anti_nodes(value, anti_nodes)

for row in anti_nodes:
    print(row)
print(sum([sum(row) for row in anti_nodes]))