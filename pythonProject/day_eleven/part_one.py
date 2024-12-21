
with open("data.txt", "r") as f:
    data = [int(x) for x in f.read().strip().split(' ')]

def update_stones(stones):
    res = []
    for stone in stones:
        if stone == 0:
            res.append(1)
        elif len(str(stone)) % 2 == 0:
            left_half = str(stone)[:int(len(str(stone))/2)]
            right_half = str(stone)[int(len(str(stone))/2):]
            res.append(int(left_half))
            res.append(int(right_half))
        else:
            res.append(stone*2024)
    return res


number_blinks = 25

for i in range(number_blinks):
    data = update_stones(data)

print(len(data))
