import heapq
import os

with open("day_one/data.txt", 'r+') as f:
    lines = f.readlines()

left_nums = []
right_nums = []
for item in lines:
    left, right = item.split('  ')
    left, right = int(left), int(right)
    left_nums.append(left)
    right_nums.append(right)

counts = {}
for item in right_nums:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
res = 0

for item in left_nums:
    if item in counts:
        res += item * counts[item]
print(res)