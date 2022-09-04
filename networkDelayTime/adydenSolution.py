
def networkDelayTime(times, n, k):
    #  [0] = []
    #  [1] = [(0,1), (2, 1)]
    #  [2] = [(3,1)]
    #  [3] = []
    graph = [[]] * n  # [[] for _ in range(n-1)]
    determined, values, checking = [False] * n, [float('inf')] * n, [i for i in range(n)]
    for x in times:
        if len(graph[x[0] - 1]) == 0:
            graph[x[0] - 1] = []
        graph[x[0] - 1].append((x[1] - 1, x[2]))
    current = k - 1
    if len(graph[current])<1:
        return -1

    values[current] = 0
    for _ in range(n):
        # find the smallest weight node from values
        t = -1
        for index in range(n):
            if not determined[index] and (t == -1 or values[index] < values[t]):
                t = index
        nodes = graph[t]
        determined[t] = True
        for i, node in enumerate(nodes):
            values[node[0]] = min(values[node[0]], values[t] + graph[t][i][1])
    return max(values)
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))