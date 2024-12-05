

with open("day_two/data.txt", "r+") as f:
    lines = f.readlines()


# def is_safe_too(row, skip_idx):
#     if skip_idx == 0:
#         is_increasing = True if row[1] < row[2] else 0
#     elif skip_idx == 1:
#         is_increasing = True if row[2] < row[3] else 0
#     else:
#         is_increasing = True if row[0] < row[1] else 0
#
#     for i in range(len(row) - 1):
#         if i == skip_idx:
#             continue
#         if abs(row[i] - row[i + 1]) < 1 or 3 < abs(row[i] - row[i + 1]):
#             return False
#         if is_increasing and row[i] > row[i + 1]:
#             return False
#         if not is_increasing and row[i] < row[i + 1]:
#             return False
#     return True

def is_safe(row):
    # Is decreasing or increasing and only differ by 2-3
    # Now we can remove one level and have it still be safe
    # Assume that we can be greedy about the level to be removed
    # How do we know which of the two indices is the problem ? Try both

    is_increasing = True if row[0] < row[1] else 0
    failure_count = 0
    i = 0
    while i < len(row)-1:
        if abs(row[i]-row[i+1]) < 1 or 3 < abs(row[i]-row[i+1]):
            failure_count += 1
            i += 1
        if is_increasing and row[i] > row[i+1]:
            failure_count += 1
            i += 1
        if not is_increasing and row[i] < row[i+1]:
            failure_count += 1
            i += 1
        i += 1
    return True


data = [[int(x) for x in line.split(' ')] for line in lines]


count = 0
for report in data:
    count += 1 if is_safe(report) else 0

print(count)