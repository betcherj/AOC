

with open("data.txt", "r") as f:
    lines = f.readlines()
    data = [[x for x in line.strip().split("-")] for line in lines]

graph = {}
for x, y in data:
    if x == y:
        continue
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

# Need to find unique groups of three
# Not easy to check a set of touples/lists
# We could iterate over each node and find every three length path for it, remove it from consideration and continue
# O(1) for the hash search, not sure worst case on the num checks but it is possibly O(n)
def find_three_deep_sets(path, graph, depth, checked_nodes):
    # They all need to be connected ..
    if depth == 3:
        return [path]
    if path[-1] in checked_nodes:
        return []

    res = []
    for item in graph[path[-1]]:
        if item not in path and item not in checked_nodes:
            res += find_three_deep_sets(path.copy() + [item], graph, depth + 1, checked_nodes)

    return res

def each_connected(triplet, graph):
    a, b, c = triplet
    if a not in graph or b not in graph or c not in graph:
        return False
    if b not in graph[a] or c not in graph[a]:
        return False
    if a not in graph[b] or c not in graph[b]:
        return False
    if a not in graph[c] or b not in graph[c]:
        return False
    return True
def count_ts(triplets):
    for node in triplets:
        if node[0] == 't':
            return True
    else:
        return False

checked_nodes = {}
all_nodes = graph.keys()
triplets = []
for node in all_nodes:
    # check three levels deep and get rows
    row =  find_three_deep_sets([node], graph, 1, checked_nodes)
    # import pdb; pdb.set_trace()

    # need to flatten here ..

    row = [item for item in row if each_connected(item, graph)]
    checked_nodes[node] = 1
    triplets += row
# We have non unique triplets !!!
# We will have exactly double

# for triplet in triplets:
#     print(triplet)
print(len(triplets)/2)
result = [item for item in triplets if count_ts(item)]
print(len(result)/2)