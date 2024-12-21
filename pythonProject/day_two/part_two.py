

with open("data.txt", "r+") as f:
    lines = f.readlines()


def is_safe(row):
    # Is decreasing or increasing and only differ by 2-3
    # We can skip one number for every row
    is_increasing = True if row[0] < row[1] else 0
    used_skip = False
    res = True
    for i in range(len(row)-1):
        if abs(row[i]-row[i+1]) < 1 or 3 < abs(row[i]-row[i+1]) :
            res = False
        if is_increasing and row[i] > row[i+1]:
            res = False
        if not is_increasing and row[i] < row[i+1]:
            res = False

        if not used_skip and res == False:
            #Need to try removing both ..
            print(f"skipping {i}")
            # i += 1
            used_skip = True
            res = True

            if i + 1 < len(row):
                is_increasing = True if row[i+1] < row[i+1] else 0

    return res


data = [[int(x) for x in line.split(' ')] for line in lines]


count = 0
for report in data:
    count += 1 if is_safe(report) else 0

print(count)