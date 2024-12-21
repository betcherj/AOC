
operators = ["*", "+", "||"]


def can_evaluate(target, nums):
    if len(nums) == 1:
        return True if nums[0] == target else False
    elif nums[0] > target:
        return False
    con_nums = [int(str(nums[0]) + str(nums[1]))] + nums[2:]
    mul_nums = [nums[0] * nums[1]] + nums[2:]
    add_nums = [nums[0] + nums[1]] + nums[2:]
    return can_evaluate(target, mul_nums) or can_evaluate(target, add_nums) or can_evaluate(target, con_nums)

with open("data.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    result, nums = data[i].strip().split(':')
    nums_list = [int(x) for x in nums.strip().split(' ')]
    data[i] = [nums_list, int(result)]


res = 0
for nums, target in data:
    res += target if can_evaluate(target, nums) else 0

print(res)


