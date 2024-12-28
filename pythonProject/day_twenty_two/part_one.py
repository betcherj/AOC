
import math
secret_num = 123


def calculate_nth_secret(n, secret_num):
    for i in range(n):
        # times 64 then mix then prune
        secret_num = ((64*secret_num) ^ secret_num)  % 16777216
        # divided by 32 then mix then prune
        secret_num = (math.floor((secret_num/32)) ^ secret_num)  % 16777216

        # multiply by 2048 then mix then prune
        secret_num = ((2048*secret_num) ^ secret_num)  % 16777216

    return secret_num

with open('data.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
n = 2000
res = 0
for num in data:
    num_res = calculate_nth_secret(n, int(num))
    print(num_res)
    res += num_res
print(res)