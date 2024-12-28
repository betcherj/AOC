

with open('data.txt', "r") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = [x.strip() for x in patterns.strip().split(",")]
    designs = [x.strip() for x in designs.strip().split('\n')]

def num_combinations(patterns, design, memo):
    # Want total number of ways to capture
    if design in memo:
        return memo[design]
    res = 0
    for pattern in patterns:
        if pattern == design:
            res += 1
        elif len(pattern) < len(design) and design[:len(pattern)] == pattern:
            res += num_combinations(patterns, design[len(pattern):], memo)
    memo[design] = res
    return res


# Brute force -> try to finish the design with every available pattern
res = 0
for row in designs:
    res += num_combinations(patterns, row, {})
print(res)