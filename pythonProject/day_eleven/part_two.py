from time import time

with open("data.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(' ')]


def update_stone(stone, remaining_updates, memo):
    if remaining_updates == 0:
        return 1

    if (stone, remaining_updates) in memo:
        return memo[(stone, remaining_updates)]

    if stone == 0:
        res = update_stone(1, remaining_updates-1, memo)
    elif len(str(stone)) % 2 == 0:
            left_half = str(stone)[:int(len(str(stone))/2)]
            right_half = str(stone)[int(len(str(stone))/2):]
            right_res = int(left_half)
            left_res = int(right_half)
            res = update_stone(left_res, remaining_updates-1, memo) + update_stone(right_res, remaining_updates-1, memo)
    else:
        res = update_stone(stone * 2024, remaining_updates-1, memo)
    memo[(stone, remaining_updates)] = res
    return res

number_blinks = 75
res = 0
from time import time
start = time()
for i in range(len(data)):
    res += update_stone(data[i], number_blinks, {})
end = time()
print(f"Took : {round(start - end)%60}s")
print(res)
