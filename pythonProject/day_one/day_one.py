import heapq
import os

with open("day_one/data.txt", 'r+') as f:
    lines = f.readlines()

left_nums = []
right_nums = []
for item in lines:
    left, right = item.split('  ')
    left, right = int(left), int(right)
    heapq.heappush(left_nums, left)
    heapq.heappush(right_nums, right)
solution = 0
for i in range(len(right_nums)):
    right = heapq.heappop(right_nums)
    left = heapq.heappop(left_nums)
    solution += abs(left-right)

print(solution)