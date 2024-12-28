

with open('data.txt', "r") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = [x.strip() for x in patterns.strip().split(",")]
    designs = [x.strip() for x in designs.strip().split('\n')]

def can_create(patterns, design, memo):
    if design in memo:
        return memo[design]
    res = False
    for pattern in patterns:
        if pattern == design:
            res = True
            break
        if len(pattern) < len(design) and design[:len(pattern)] == pattern:
            res = res or can_create(patterns, design[len(pattern):], memo)
    memo[design] = res
    return res


# Brute force -> try to finish the design with every available pattern
res = 0
for row in designs:
    res += 1 if can_create(patterns, row, {}) else 0
print(res)