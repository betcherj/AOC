import re
maximum_button_pressed = 100

with open("data.txt", "r") as f:
    raw_data = [[x for x in line.strip().split("\n")] for line in f.read().split("\n\n")]

def calculate_cost(pos, num_presses_A, num_presses_B, numbers_A, numbers_B, target, memo):
    "For a given target calculate the cost of getting there with button presses"
    # IF we have pressed a button more than 100 times we ca stop pressing it
    if pos in memo:
        return memo[pos]
    x_a, x_b = numbers_A
    if pos[0] + x_a <= target and pos[1] + x_b <= target:
        # Try pressing the A button
        pass





data = []
for row in raw_data:
    button_A_str = row[0]
    numbers_A =  [int(x) for x in re.findall(r'\d+', button_A_str)]
    button_B_str = row[1]
    numbers_B =  [int(x) for x in re.findall(r'\d+', button_B_str)]
    prize = row[2]
    numbers_prize = [int(x) for x in re.findall(r'[+-]?\d+', prize)]
    data.append([numbers_A, numbers_B, numbers_prize])


for row in data:
    numbers_A, numbers_B, numbers_prize = row