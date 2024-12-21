

with open("data.txt", "r+") as f:
    lines = f.readlines()


def is_safe(row):
    # Is decreasing or increasing and only differ by 2-3
    is_increasing = True if row[0] < row[1] else 0
    for i in range(len(row)-1):
        if abs(row[i]-row[i+1]) < 1 or 3 < abs(row[i]-row[i+1]) :
            return False
        if is_increasing and row[i] > row[i+1]:
            return False
        if not is_increasing and row[i] < row[i+1]:
            return False
    return True


data = [[int(x) for x in line.split(' ')] for line in lines]


count = 0
for report in data:
    count += 1 if is_safe(report) else 0

print(count)